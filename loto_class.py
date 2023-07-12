import random

# Генерация мешка с бочонками
def generate_kegs():
    kegs = []
    [kegs.append(i) for i in range(1, 91)]
    random.shuffle(kegs)
    return kegs


# Карточка с цифрами
class Card:
    def __init__(self):
        self.spisok_num = random.sample(range(1, 91), 15)
        self.card_nums = []
        self.create_card()

    # создание карточки с цифрами
    def create_card(self):
        spisok0 = self.spisok_num

        for i in range(0, 3):
            num_col = random.sample(range(0, 9), 9)
            spisok, num = [], 0
            [spisok.append(" ") for j in range(0, 9)]
            for col in num_col:
                if num < 5:
                    spisok[col] = spisok0[num]
                    num += 1
            spisok0 = spisok0[5:]
            self.card_nums.append(spisok)

    # замена числа в карточке на символ "-" и удаление числа из списка чисел этой карточки
    def cross_num(self, number):
        for item in self.card_nums:
            try:
                index = item.index(number)
                item[index] = "- "
                self.spisok_num.remove(number)
                break
            except ValueError:
                pass

    # проверка все ли числа в карточке зачеркнуты
    def closed(self):
        answer = len(self.spisok_num)
        return answer

    # вывод карточки
    def print_card(self):
        s = ''
        for item in self.card_nums:
            for num in item:
                s += str(num) + " "
                if isinstance(num, int) and item.index(num) != len(item):
                    s += " "
            s += "\n"
        return s
# Игра
class Game:

    def __init__(self):
        self.usercard = Card()
        self.compcard = Card()
        self.kegs = generate_kegs()

    # вытаскивается бочонок из мешка
    def play_round(self):
        keg = self.kegs.pop()
        print(f"Новый бочонок: {keg} (осталось {len(self.kegs)})\n")
        print(f"----- Ваша карточка ------\n{self.usercard.print_card()}")
        print(f"-- Карточка компьютера ---\n{self.compcard.print_card()}")

        answer = input("Зачеркнуть цифру? (да/нет) ").lower().strip()
        if (answer == "да" and not keg in self.usercard.spisok_num) or (answer != "да" and keg in self.usercard.spisok_num):
            return 2


        if keg in self.usercard.spisok_num:
            self.usercard.cross_num(keg)
            if self.usercard.closed():
                return 1

        if keg in self.compcard.spisok_num:
            self.compcard.cross_num(keg)
            if self.compcard.closed():
                return 2

        return 0

# if __name__ == "__main__":
#     # card = Card()
#     # card.create_card(card.spisok_num)
#
#     game = Game()
#     while True:
#         score = game.play_round()
#         if score == 1:
#             print("Вы выиграли! Поздравляем")
#             break
#         elif score == 2:
#             print("К сожалению вы проиграли :(")
#             break
