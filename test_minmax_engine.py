from minmax_engine import start_engine


def main():
    # lorder_cards = [2, 2, 'A', 'K', 10, 7, 6, 6, 5, 5, 4, 3]
    # farmer_cards = ['Z', 2, 'A', 'K', 'Q', 'J', 10, 5, 5, 4, 3]
    # best_move = start_engine(lorder_cards=lorder_cards, farmer_cards=farmer_cards, farmer_move=[])

    lorder_cards = ['A', 'A', 'K', 'J', 9, 9, 8, 6, 4]
    farmer_cards = ['2', 'A', 'J', 10, 10, 7, 7, 6, 5, 5, 4, 3, 3]
    best_move = start_engine(lorder_cards=lorder_cards, farmer_cards=farmer_cards, farmer_move=[])
    print("Best Move is %s" % best_move)


if __name__ == '__main__':
    # freeze_support()
    main()
