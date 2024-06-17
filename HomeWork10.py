class Bank:
    def  __init__(self):
        self.account = None

    def OpenAcc(self):
        self.account = 0
        print("Счет открыт")

    def ClouseAcc(self):
        self.account = None
        print("Счет закрыт")

    def deposit(self, amount):
        if self.account is not None:
            self.account += amount
            print(f"На счет поступило {amount} руб")
        else:
            print("счет не открыт, пополнение невозможно")


    def windraw(self, amount):
        if self.account is not None:
            if amount <= self.account:
                self.account -= amount
                print(f"со счета снято {amount} руб")
            else:
                print("not money")

        else:
            print("счет не открыт")


bankAcc = Bank()
bankAcc.OpenAcc()
bankAcc.deposit(1200)
bankAcc.windraw(500)
bankAcc.ClouseAcc()



class Restoran:
    def __init__(self):
        self.menu = []


    def addDish(self, dish):
        self.menu.append(dish)
        print(f"блюдо {dish} добавлено в меню")


    def DelDish(self, dish):
        if dish in self.menu:
            self.menu.remove(dish)
            print(f"блюдо {dish} удалено из меню")
        else:
            print(f"блюдо {dish} нет в меню")

    def order(self, OrderList):
        print("you order")
        for dish in OrderList:
            if dish in self.menu:
                print(f" * {dish}")
            else:
                print(f"блюдо {dish} отсутствует в меню ")


restauran = Restoran()
restauran.addDish("Borsh")
restauran.addDish("Rollton")
restauran.DelDish("Borsh")
restauran.order(["Rollton", "winston"])