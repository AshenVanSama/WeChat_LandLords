import move_classifier
from common import format_input, GenAnyN, print_func_name, get_rest_cards
from move_gener import MovesGener
from ui_engine import UIEngine
from move_player import get_possible_moves, do_a_move

a = [3, 3, 3, 4, 4, 4, 6, 7, 8, 9, 10, 10, 'K']
b = [6, 7, 8, 9, 10, 'J', 'J', 'Q', 'Q', 'Q', 'Y']
c = [3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 11, 12, 13, 13, 13, 14, 14, 14, 'Y', 'Z']


@print_func_name
def test_MoveGener():
    print(format_input(c))
    mg = MovesGener(format_input(c))
    moves = mg.gen_moves()
    # print(moves)
    print(len(moves))


@print_func_name
def test_gen_type_8_serial_single():
    mg = MovesGener(format_input(c))
    print(mg.gen_type_8_serial_single(repeat_num=7))


@print_func_name
def test_gen_type_9_serial_pair():
    mg = MovesGener(format_input(c))
    print(mg.gen_type_9_serial_pair(repeat_num=5))


@print_func_name
def test_gen_type_10_serial_triple():
    mg = MovesGener(format_input(c))
    print(mg.gen_type_10_serial_triple(repeat_num=2))


@print_func_name
def test_gen_type_11_serial_3_1():
    mg = MovesGener(format_input(c))
    print(mg.gen_type_11_serial_3_1())


@print_func_name
def test_gen_type_12_serial_3_2():
    mg = MovesGener(format_input(c))
    print(mg.gen_type_12_serial_3_2())


@print_func_name
def test_GenAnyN():
    gan = GenAnyN([1, 2, 3, 4, 5], 3)  # from this list, get any 3 numbers
    result = gan.gen_n_cards_lists()
    for cards in result:
        print(cards)
    print(len(result))


@print_func_name
def test_MoveClassifier():
    moves = [
        [],
        [20],
        [3, 3],
        [20, 30],
        [4, 4, 4],
        [5, 5, 5, 2],
        [3, 3, 3, 5],
        [6, 3, 4, 5],
        [6, 6, 6, 6],
        [7, 7, 7, 8, 8],
        [9, 9, 10, 10, 10],
        [3, 4, 5, 6, 7],
        [3, 4, 5, 6, 8],
        [2, 2, 4, 5, 6],
        [3, 4, 5, 6, 7, 8, 9],
        [3, 3, 3, 3, 5, 6],
        [3, 3, 3, 3, 5, 6, 7],
        [4, 4, 4, 4, 5, 5, 7, 7],
        [4, 4, 4, 4, 5, 5, 7, 6],
        [4, 4, 4, 4, 5, 5, 6, 6, 7, 7],
        [5, 5, 5, 6, 6, 6, 7, 8],
        [5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9, 10],
        [5, 5, 5, 6, 6, 6, 7, 7, 9, 9],
        [5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 10, 10, 13, 13],
        [5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 10, 10, 13, 13, 14],
    ]

    mc = move_classifier.MoveClassifier()
    count = 0
    for move in moves:
        count += 1
        move_type = mc.get_move_type(move).get('type')
        print("%d: The type of %s is %s" %
              (count,
               move,
               move_classifier.MOVE_TYPES_STR.get(move_type, "Wrong")))


@print_func_name
def test_ui_engine():
    ui_engine = UIEngine()
    ui_engine.run()


@print_func_name
def test_get_possible_moves():
    rival_move = [3, 3, 4, 4, 5, 5]
    cards = [5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 20, 30]
    print("moves = %s" % get_possible_moves(cards, rival_move))

    rival_move = [5, 5, 5, 6, 6, 6, 7, 8]
    cards = [7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 11, 12, 20, 30]
    print("moves = %s" % get_possible_moves(cards, rival_move))


@print_func_name
def test_do_interact_moves():
    lord_cards = [2, 3, 4, 5, 5, 7, 7]
    farmer_cards = [3, 6, 9, 9, 10, 4]
    player = 'lord'

    move = do_a_move(lord_cards=lord_cards,
                     farmer_cards=farmer_cards,
                     previous_move=[],
                     player=player)
    lord_cards = get_rest_cards(lord_cards, move)
    previous_move = move

    while lord_cards and farmer_cards:
        player = 'farmer' if player == 'lord' else 'lord'

        move = do_a_move(lord_cards=lord_cards,
                         farmer_cards=farmer_cards,
                         previous_move=previous_move,
                         player=player)

        if player == 'farmer':
            farmer_cards = get_rest_cards(farmer_cards, move)
            if not farmer_cards:
                print("Farmer Win!")
                break
        else:
            lord_cards = get_rest_cards(lord_cards, move)
            if not lord_cards:
                print("LandLord Win!")
                break

        previous_move = move


def main():
    test_MoveGener()
    test_gen_type_8_serial_single()
    test_gen_type_9_serial_pair()
    test_gen_type_10_serial_triple()
    test_gen_type_11_serial_3_1()
    test_gen_type_12_serial_3_2()
    test_GenAnyN()
    test_MoveClassifier()
    # test_ui_engine()
    test_get_possible_moves()
    test_do_interact_moves()


main()
