import itertools
from card import Card
from deck import Deck
from lookup import LookupTable

class Evaluator(object):
    """
    Evaluates hand strengths using a variant of Cactus Kev's algorithm:
    http://www.suffecool.net/poker/evaluator.html

    I make considerable optimizations in terms of speed and memory usage, 
    in fact the lookup table generation can be done in under a second and 
    consequent evaluations are very fast. Won't beat C, but very fast as 
    all calculations are done with bit arithmetic and table lookups. 
    """

    def __init__(self):

        self.table = LookupTable()
        
        self.hand_size_map = {
            5 : self._five,
            6 : self._more_than_five,
            7 : self._more_than_five
        }

    def evaluate(self, cards, board):
        """
        This is the function that the user calls to get a hand rank. 

        Supports empty board, etc very flexible. No input validation 
        because that's cycles!
        """
        return self.best_hand(cards, board)[0]

    def best_hand(self, cards, board):
        """
        Like evaluate, except that both the rank and the 5 cards that
        make up the best possible hand are returned togther as a tuple.
        """
        all_cards = cards + board
        return self.hand_size_map[len(all_cards)](all_cards)

    def _five(self, cards):
        """
        Performs an evalution given cards in integer form, mapping them to
        a rank in the range [1, 7462], with lower ranks being more powerful.

        Variant of Cactus Kev's 5 card evaluator, though I saved a lot of memory
        space using a hash table and condensing some of the calculations. 
        """
        # if flush
        if cards[0] & cards[1] & cards[2] & cards[3] & cards[4] & 0xF000:
            handOR = (cards[0] | cards[1] | cards[2] | cards[3] | cards[4]) >> 16
            prime = Card.prime_product_from_rankbits(handOR)
            return self.table.flush_lookup[prime], cards

        # otherwise
        else:
            prime = Card.prime_product_from_hand(cards)
            return self.table.unsuited_lookup[prime], cards

    def _more_than_five(self, cards):
        """
        Performs five_card_eval() on all subsets of 5 cards in the set to
        determine the best ranking, and returns this ranking and the
        hand itself.
        """
        minimum = LookupTable.MAX_HIGH_CARD
        best_hand = None

        all5cardcombos = itertools.combinations(cards, 5)
        for combo in all5cardcombos:

            score, hand = self._five(combo)
            if score < minimum:
                minimum = score
                best_hand = combo

        return minimum, best_hand

    def get_rank_class(self, hr):
        """
        Returns the class of hand given the hand hand_rank
        returned from evaluate. 
        """
        if hr >= 0 and hr < LookupTable.MAX_STRAIGHT_FLUSH:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_STRAIGHT_FLUSH]
        elif hr <= LookupTable.MAX_FOUR_OF_A_KIND:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_FOUR_OF_A_KIND]
        elif hr <= LookupTable.MAX_FULL_HOUSE:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_FULL_HOUSE]
        elif hr <= LookupTable.MAX_FLUSH:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_FLUSH]
        elif hr <= LookupTable.MAX_STRAIGHT:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_STRAIGHT]
        elif hr <= LookupTable.MAX_THREE_OF_A_KIND:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_THREE_OF_A_KIND]
        elif hr <= LookupTable.MAX_TWO_PAIR:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_TWO_PAIR]
        elif hr <= LookupTable.MAX_PAIR:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_PAIR]
        elif hr <= LookupTable.MAX_HIGH_CARD:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_HIGH_CARD]
        else:
            raise Exception("Inavlid hand rank, cannot return rank class")

    def class_to_string(self, class_int):
        """
        Converts the integer class hand score into a human-readable string.
        """
        return LookupTable.RANK_CLASS_TO_STRING[class_int]

    def get_five_card_rank_percentage(self, hand_rank):
        """
        Scales the hand rank score to the [0.0, 1.0] range.
        """
        return float(hand_rank) / float(LookupTable.MAX_HIGH_CARD)

    def hand_summary(self, board, hands):
        """
        Gives a sumamry of the hand with ranks as time proceeds. 

        Requires that the board is in chronological order for the 
        analysis to make sense.
        """

        assert len(board) == 5, "Invalid board length"
        for hand in hands:
            assert len(hand) == 2, "Inavlid hand length"

        line_length = 10
        stages = ["FLOP", "TURN", "RIVER"]

        for i in range(len(stages)):
            line = ("=" * line_length) + " %s " + ("=" * line_length) 
            print line % stages[i]
            
            counter = 1 
            ranks = []
            for hand in hands:
                rank = self.evaluate(hand, board[:(i + 3)])
                rank_class = self.get_rank_class(rank)
                class_string = self.class_to_string(rank_class)
                percentage = self.get_five_card_rank_percentage(rank)
                ranks.append(rank)
                print "Player %d hand = %s, percentage rank among all hands = %f" % (counter, class_string, percentage)

                counter += 1

            winner = ranks.index(min(ranks)) + 1
            if i != 2:
                print "Player %d hand is currently winning." % winner
            else:
                print
                print ("=" * line_length) + " HAND OVER " + ("=" * line_length) 
                print "Player %d is the winner with a %s" % (winner, self.class_to_string(self.get_rank_class(self.evaluate(hands[winner-1], board))))
            
            print



