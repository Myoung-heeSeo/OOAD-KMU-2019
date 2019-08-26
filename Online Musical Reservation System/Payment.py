import CreditCard
import OrderInfo
import Seat

class Payment:
    def __init__(self, BookTicket):
        self.order = OrderInfo.OrderInfo()
        self.amount= 0
        self.creditCard=0
        self.getCardInfo(BookTicket)

    def getCardInfo(self, BookTicket):
        print("Enter the card number(16)")
        cnum=input()
        self.creditCard = CreditCard.CreditCard(cnum)
        self.getOrderInfo(BookTicket)

    def getOrderInfo(self, BookTicket):
        self.order.getOrderInfo(BookTicket.oid)
        self.calculateAmount()


    def calculateAmount(self):
        self.amount = self.order.price
        self.requestPayment()

    def requestPayment(self):
        print("  Payment Success!")
        self.changeSeatStatus()
        self.sendEticket()

    def changeSeatStatus(self):
        seat=Seat.Seat()
        seat.getSeatInfo(self.order.mid)
        seat.changeSeatStatus(self.order.seatNo)

    def sendEticket(self):
        print("  Successfully send Eticket!")