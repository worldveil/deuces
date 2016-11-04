import time
from SevenEval import SevenEval
from FiveEval import FiveEval
import random

def setup(n, m):

    hands = []
    boards = []
    
    for i in range(n):

        deck = list(range(52))
        random.shuffle(deck)
        hand = []
        board = []
        for j in range(2):
            hand.append(deck.pop(0))
        for j in range(m):
            board.append(deck.pop(0))

        hands.append(hand)
        boards.append(board)

    return boards, hands

s = SevenEval()

N = 10000
cumtime = 0.0
boards, hands = setup(N, 5)
for i in range(len(boards)):
    start = time.time()
    s.getRankOfSeven(*(boards[i] + hands[i]))
    cumtime += (time.time() - start)

avg = float(cumtime / N)
print("7 card evaluation:")
print("[*] SpecialK: Average time per evaluation: %f" % avg)
print("[*] SpecialK: Evaluations per second = %f" % (1.0 / avg))

####

f = FiveEval()

cumtime = 0.0
boards, hands = setup(N, 3)
for i in range(len(boards)):
    start = time.time()
    f.getRankOfFive(*(boards[i] + hands[i]))
    cumtime += (time.time() - start)

avg = float(cumtime / N)
print("5 card evaluation:")
print("[*] SpecialK: Average time per evaluation: %f" % avg)
print("[*] SpecialK: Evaluations per second = %f" % (1.0 / avg))