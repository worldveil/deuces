import mock

from . import Card, Evaluator, Deck


EXAMPLE = (
    (Card.new('4c'), Card.new('As'), Card.new('5d'), Card.new('Kc'), Card.new('2s')),
    (Card.new('6c'), Card.new('7h')),
    (Card.new('Ac'), Card.new('3h')),
)

def test_go():
    """Does the example from the README.md run correctly?"""
    # create a card
    card = Card.new('Qh')
    assert card is not None

    # create a board and hole cards
    board = [
        Card.new('2h'),
        Card.new('2s'),
        Card.new('Jc')
    ]
    hand = [
        Card.new('Qs'),
        Card.new('Th')
    ]

    # pretty print cards to console
    Card.print_pretty_cards(board + hand)

    # create an evaluator
    evaluator = Evaluator()

    # and rank your hand
    rank = evaluator.evaluate(board, hand)
    print(f"Rank for your hand is: {rank}")
    assert rank == 6066

    print("Dealing a new hand...")
    deck = Deck()
    deck.draw = mock.Mock(side_effect=EXAMPLE)
    board = deck.draw(5)
    player1_hand = deck.draw(2)
    player2_hand = deck.draw(2)

    print("The board:")
    Card.print_pretty_cards(board)

    print("Player 1's cards:")
    Card.print_pretty_cards(player1_hand)

    print("Player 2's cards:")
    Card.print_pretty_cards(player2_hand)

    p1_score = evaluator.evaluate(board, player1_hand)
    p2_score = evaluator.evaluate(board, player2_hand)
    assert p1_score == 6330
    assert p2_score == 1609

    # bin the scores into classes
    p1_class = evaluator.get_rank_class(p1_score)
    p2_class = evaluator.get_rank_class(p2_score)

    # or get a human-friendly string to describe the score
    print("Player 1 hand rank = %d (%s)" % (p1_score, evaluator.class_to_string(p1_class)))
    print("Player 2 hand rank = %d (%s)" % (p2_score, evaluator.class_to_string(p2_class)))
    assert evaluator.class_to_string(p1_class) == 'High Card'
    assert evaluator.class_to_string(p2_class) == 'Straight'

    # or just a summary of the entire hand
    hands = [player1_hand, player2_hand]
    evaluator.hand_summary(board, hands)
