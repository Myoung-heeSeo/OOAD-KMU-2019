import CardType

class CreditCard:
    cardType = CardType

    def __init__(self, cardnum):
        self.cardType=2
        self.cardNum = cardnum
        self.signal = True

    def getPaymentSignal(self):
        print("get Payment Signal from Card!")
    def checkCardType(self):
        return

