import OrderInfo
import CancelTicket
import PersonalInfo
import Musical

class CheckMyTicket():
    def __init__(self):
        self.TicketHistory=list()
        self.PersonalInfo=PersonalInfo.PersonalInfo()

    def checkPersonalInfo(self, website):
        print(">> Enter your name")
        name=input()
        self.PersonalInfo.getCustomer(name)
        if self.PersonalInfo.name=='':
            self.checkPersonalInfo(website)
        else :
            self.findMyTicket()
            self.displayTicketHistory(website)




    def displayTicketHistory(self, website):
        print("=" * 91)
        print(" " * 37 + "Ticket History" + " " * 37)
        print("=" * 91)
        print("Customer Name: "+ self.PersonalInfo.name+ ' '*20+"phone number: "+ self.PersonalInfo.phoneNum)
        print("=" * 91)
        print("OrderID "+ "Musical Name              "+"Date            "+"Time   "+"Theatre              ""SeatNo "+"Price ")
        print("="*7+' '+'='*25+' '+'='*15+' '+'='*6+' '+'='*20+' '+'='*6+' '+'='*6)
        for obj in self.TicketHistory:
            musical=Musical.Musical()
            musical.getMusicalObject(obj.mid)
            print(str(obj.id)+' '*(7-len(str(obj.id)))+musical.name+' '*(26-len(musical.name))+
                  musical.date+' '*(16-len(musical.date))+musical.time+' '*(7-len(musical.time))
                  +musical.theatre+' '*(22-len(musical.theatre))+str(obj.seatNo)+' '*(6-len(str(obj.seatNo)))+obj.price)
        print("=" * 91)
        print(">> Enter the option")
        print("   1: Cancel the Ticket")
        print("   2: Back to Home")
        option=int(input())
        if option==1:
            self.cancelTicket(website)
        else:
            website.start()


    def cancelTicket(self, website):
        print(" >> Enter the orderID to cancel")
        orderid = int(input())
        cancel=CancelTicket.CancelTicket(self, website, orderid)



    def findMyTicket(self):

        f = open('Order.txt', 'r')
        for line in f:
            data = line.split(',')
            if str(data[1][1:]) == str(self.PersonalInfo.name):
                order= OrderInfo.OrderInfo()
                order.id = int(data[0])
                order.personal.getCustomer(data[1][1:])
                order.mid = int(data[2])
                order.seatNo = int(data[3])
                order.eticket = int(data[4])
                order.price = data[5]
                self.TicketHistory.append(order)



