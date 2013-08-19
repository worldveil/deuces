from card import Card
from hand_evaluator import HandEvaluator
import time
import random

def setup(n):

    hands = []
    boards = []

    full_deck = []
    for i in range(2, 14 + 1):
        for j in range(1, 4 + 1):
            full_deck.append(Card(i, j))


    for i in range(n):

        deck = list(full_deck)
        random.shuffle(deck)
        hand = []
        board = []
        for j in range(2):
            hand.append(deck.pop(0))
        for j in range(5):
            board.append(deck.pop(0))

        hands.append(hand)
        boards.append(board)

    return boards, hands

N = 10000
cumtime = 0.0
boards, hands = setup(N)
for i in range(len(boards)):
    start = time.time()
    HandEvaluator.evaluate_hand(hands[i], boards[i])
    cumtime += (time.time() - start)

avg = float(cumtime / N)
print "[*] Pokerhand-eval: Average time per evaluation: %f" % avg
print "[*] Pokerhand-eval: Evaluations per second = %f" % (1.0 / avg)