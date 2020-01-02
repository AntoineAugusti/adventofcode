import unittest
from collections import defaultdict
import math


def parse_input(input):
    def parse_src(src):
        res = {}
        for el in src.split(","):
            el = el.strip()
            quantity, el = el.split(" ")
            res[el] = int(quantity)
        return res

    res = {}
    for line in input.split("\n"):
        line = line.strip()
        if len(line) == 0:
            continue
        src, dst = [p.strip() for p in line.split("=>")]
        quantity, dst = dst.split(" ")
        res[dst] = {"quantity": int(quantity), "ingredients": parse_src(src)}

    return res


def produce(orders, recipies, supply):
    amount, chem = orders.pop(0)

    if chem == "ORE":
        supply["ORE"] += amount
        return

    if amount <= supply[chem]:
        supply[chem] -= amount
        return

    amount_needed = amount - supply[chem]
    reactions_needed = math.ceil(amount_needed / recipies[chem]["quantity"])

    for ingredient, quantity in recipies[chem]["ingredients"].items():
        orders.append((quantity * reactions_needed, ingredient))
        produce(orders, recipies, supply)

    supply[chem] += reactions_needed * recipies[chem]["quantity"] - amount


def count_ore(input):
    orders = [(1, "FUEL")]
    supply = defaultdict(int)
    produce(orders, parse_input(input), supply)
    return supply["ORE"]


class Test(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual(
            {
                "A": {"quantity": 2, "ingredients": {"ORE": 9}},
                "B": {"quantity": 3, "ingredients": {"ORE": 8}},
                "C": {"quantity": 5, "ingredients": {"ORE": 7}},
                "AB": {"quantity": 1, "ingredients": {"A": 3, "B": 4}},
                "BC": {"quantity": 1, "ingredients": {"B": 5, "C": 7}},
                "CA": {"quantity": 1, "ingredients": {"C": 4, "A": 1}},
                "FUEL": {"quantity": 1, "ingredients": {"AB": 2, "BC": 3, "CA": 4}},
            },
            parse_input(
                """
        9 ORE => 2 A
        8 ORE => 3 B
        7 ORE => 5 C
        3 A, 4 B => 1 AB
        5 B, 7 C => 1 BC
        4 C, 1 A => 1 CA
        2 AB, 3 BC, 4 CA => 1 FUEL
        """
            ),
        )

    def test_count_ore(self):
        self.assertEqual(
            165,
            count_ore(
                """
        9 ORE => 2 A
        8 ORE => 3 B
        7 ORE => 5 C
        3 A, 4 B => 1 AB
        5 B, 7 C => 1 BC
        4 C, 1 A => 1 CA
        2 AB, 3 BC, 4 CA => 1 FUEL
        """
            ),
        )
        self.assertEqual(
            13312,
            count_ore(
                """
        157 ORE => 5 NZVS
        165 ORE => 6 DCFZ
        44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
        12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
        179 ORE => 7 PSHF
        177 ORE => 5 HKGWZ
        7 DCFZ, 7 PSHF => 2 XJWVT
        165 ORE => 2 GPVTF
        3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
        """
            ),
        )
        self.assertEqual(
            180697,
            count_ore(
                """
        2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
        17 NVRVD, 3 JNWZP => 8 VPVL
        53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
        22 VJHF, 37 MNCFX => 5 FWMGM
        139 ORE => 4 NVRVD
        144 ORE => 7 JNWZP
        5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
        5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
        145 ORE => 6 MNCFX
        1 NVRVD => 8 CXFTF
        1 VJHF, 6 MNCFX => 4 RFSQX
        176 ORE => 6 VJHF
        """
            ),
        )
        self.assertEqual(
            2210736,
            count_ore(
                """
        171 ORE => 8 CNZTR
        7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
        114 ORE => 4 BHXH
        14 VRPVC => 6 BMBT
        6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
        6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
        15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
        13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
        5 BMBT => 4 WPTQ
        189 ORE => 9 KTJDG
        1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
        12 VRPVC, 27 CNZTR => 2 XDBXC
        15 KTJDG, 12 BHXH => 5 XCVML
        3 BHXH, 2 VRPVC => 7 MZWV
        121 ORE => 7 VRPVC
        7 XCVML => 6 RJRHP
        5 BHXH, 4 VRPVC => 5 LTCX
        """
            ),
        )


if __name__ == "__main__":
    unittest.main()
