from ui_engine import UIEngine


def main():
    lorder_cards = "A A K J 9 9 8 6 4".split()
    farmer_cards = "2 A J 10 10 6 4 3 3".split()

    UIEngine.run(lorder_cards, farmer_cards)


if __name__ == '__main__':
    # freeze_support()
    main()
