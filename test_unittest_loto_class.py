import unittest
import loto_class


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = loto_class.Card()

    def test_init(self):
        self.assertEqual(len(self.card.spisok_num), 15)
        self.assertNotEqual(self.card.spisok_num, 91)

    def test_create_card(self):
        self.assertEqual(len(self.card.card_nums), 3)
        self.assertTrue(self.card.card_nums)

    def test_cross_num(self):
        spisok_num = [6, 51, 5, 86, 49, 19, 48, 42, 25, 61, 1, 45, 75, 90, 22]
        self.card.cross_num(50)
        self.assertNotIn(50, spisok_num)
        spisok_num = [6, 50, 5, 86, 49, 19, 48, 42, 25, 61, 1, 45, 75, 90, 22]
        self.assertIn(50, spisok_num)

    def test_closed(self):
        spisok_num = [6, 51, 5, 86, 49, 19, 48, 42, 25, 61, 1, 45, 75, 90, 22]
        self.card.closed()
        self.assertTrue(len(spisok_num))
        spisok_num = []
        self.assertFalse(len(spisok_num))

    def test_str(self):
        self.assertIsInstance(self.card.spisok_num, list)

    def test_eq(self):
        other = []
        self.assertFalse(other)

class TestGame(unittest.TestCase):
    def setUp(self):
        self.usercard = loto_class.Card()
        self.compcard = loto_class.Card()

    def test_init(self):
        self.assertEqual(len(loto_class.Game.generate_kegs()), 90)
        self.assertIsInstance(loto_class.Game.generate_kegs(), list)
        self.kegs = loto_class.Game.generate_kegs()
        self.assertEqual(len(self.kegs), 90)
        self.assertIsInstance(self.kegs, list)



# if __name__ == '__main__':
#     unittest.main()
