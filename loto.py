import loto_class

game = loto_class.Game()
while True:
    score = game.play_round()
    if score == 1:
        print("Вы выиграли! Поздравляем")
        break
    elif score == 2:
        print("К сожалению вы проиграли :(")
        break