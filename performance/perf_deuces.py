import time
import random
from deuces import Card, Deck, Evaluator

def setup(n, m):

    deck = Deck()

    boards = []
    hands = []

    for i in range(n):
        boards.append(deck.draw(m))
        hands.append(deck.draw(2))
        deck.shuffle()

    return boards, hands


n = 10000
cumtime = 0.0
evaluator = Evaluator()
boards, hands = setup(n, 5)
for i in range(len(boards)):
    start = time.time()
    evaluator.evaluate(boards[i], hands[i])
    cumtime += (time.time() - start)

avg = float(cumtime / n)
print "7 card evaluation:"
print "[*] Deuces: Average time per evaluation: %f" % avg
print "[*] Decues: Evaluations per second = %f" % (1.0 / avg)

###

cumtime = 0.0
boards, hands = setup(n, 4)
for i in range(len(boards)):
    start = time.time()
    evaluator.evaluate(boards[i], hands[i])
    cumtime += (time.time() - start)

avg = float(cumtime / n)
print "6 card evaluation:"
print "[*] Deuces: Average time per evaluation: %f" % avg
print "[*] Decues: Evaluations per second = %f" % (1.0 / avg)

###

cumtime = 0.0
boards, hands = setup(n, 3)
for i in range(len(boards)):
    start = time.time()
    evaluator.evaluate(boards[i], hands[i])
    cumtime += (time.time() - start)

avg = float(cumtime / n)
print "5 card evaluation:"
print "[*] Deuces: Average time per evaluation: %f" % avg
print "[*] Decues: Evaluations per second = %f" % (1.0 / avg)
