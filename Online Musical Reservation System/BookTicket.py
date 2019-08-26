import OrderInfo
import Payment
import Seat
import PersonalInfo

class BookTicket:
    def __init__(self, mid,website):
        self.MID=mid
        self.name=''
        self.phone=''
        self.seatNo=0
        self.eticket = 0
        self.oid=0
        self.findTicket(mid, website)

    def displayRemainSeats(self, mid):
        seatfile = open("Seat.txt", 'r')
        for line in seatfile:
            if mid==line[:len(str(mid))]:
                print(line)
        seatfile.close()

    def findTicket(self, mid, website):
        self.displayRemainSeats(mid)
        self.selectSeats(mid)
        self.enterPersonalInfo()
        self.selectEticket()
        self.makeOrderInfo()
        p =Payment.Payment(self)
        website.start()


    def selectEticket(self):
        print(">>Select the eticket receiving")
        print("  1: Receive")
        print("  2: Do Not Receive")
        et = int(input())
        self.eticket=et

    def selectSeats(self, mid):
        print(">>Enter the seat number to book")
        sno=int(input())
        self.seatNo=sno


    def enterPersonalInfo(self):
        print(">>Enter your name")
        self.name= input()
        print(">>Enter your phone number")
        self.phone = input()
        per=PersonalInfo.PersonalInfo()
        per.setCustomer(self.name, self.phone)


    def makeOrderInfo(self):
        f=open('Order.txt', 'r')
        oid=0
        for line in f:
            data=line.split(',')
            oid=int(data[0])+1
        self.oid=oid

        seat=Seat.Seat()
        seat.getSeatInfo(self.MID)
        price=seat.price

        order=OrderInfo.OrderInfo()
        order.setOrderInfo(self.oid, self.name, self.MID, self.seatNo, self.eticket, price)
