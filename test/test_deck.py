import unittest

from deuces.deuces import Deck


class TestDeck(unittest.TestCase):
    def test_shuffle(self):
        d1 = Deck(seed=0.1)
        d2 = Deck(seed=0.1)

        self.assertEquals(d1.draw(), d2.draw())
        self.assertEquals(1, d1.num_drawn)
        self.assertEquals(1, d2.num_drawn)

    def test_predrawn(self):
        d1 = Deck(seed=0.1)
        d2 = Deck(seed=0.1, num_drawn=2)
        self.assertEquals(0, d1.num_drawn)
        self.assertEquals(2, d2.num_drawn)

        d1.draw()
        d1.draw()
        self.assertEquals(2, d1.num_drawn)

        self.assertEquals(d1.draw(), d2.draw())

    def test_multi_draw(self):
        d1 = Deck(seed=0.1)
        d2 = Deck(seed=0.1)

        self.assertEquals(d1.draw(3), d2.draw(3))
        self.assertEquals(3, d1.num_drawn)
        self.assertEquals(3, d2.num_drawn)
