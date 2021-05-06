from Game import Game


def main():
    game = Game(9, 8, 7)

    status = Game.CONTINUE

    while status == Game.CONTINUE:
        print(game)
        print_instruction()
        action, x, y = input("Ход: ").split()
        x, y = int(x) - 1, int(y) - 1

        if action.lower() == "flag":
            game.changeFlag(x, y)

        elif action.lower() == "step":
            status = game.doStep(x, y)

        else:
            print("Неизвестное действие")

    print(game)


def print_instruction():
    print("Поставить/снять флажок: flag x y")
    print("Сделать ход: step x y")

# if __name__ == '__main__':
#    main()
