import OrderInfo
import Seat

class CancelTicket():
    def __init__(self, checkTicket, website, oid):
        self.isPossible= 0
        self.fee= ''
        self.orderID=oid
        self.musicalID=0
        self.seatNo=0
        self.checkDate()
        for ticket in checkTicket.TicketHistory:
            if ticket.id==self.orderID:
                checkTicket.TicketHistory.remove(ticket)

        checkTicket.displayTicketHistory(website)



    def checkDate(self):
        self.calculateFee()
        return

    def calculateFee(self):
        self.deleteOrderInfo()
        return
    def changeSeatStatus(self):
        seat = Seat.Seat()
        seat.getSeatInfo(int(self.musicalID))
        seat.changeSeatStatus(int(self.seatNo))
        self.requestRefund()

    def deleteOrderInfo(self):
        f= open("Order.txt", 'r')
        ordertxt = ''
        for line in f:
            data = line.split(',')
            if(self.orderID==int(data[0])):
                self.musicalID=data[2]
                self.seatNo=data[3]
            else:
                ordertxt+= line
        f.close()
        f=open("Order.txt", 'w')
        f.write(ordertxt)
        f.close()

        self.changeSeatStatus()


    def requestRefund(self):
        print("Successfully cancel the ticket")