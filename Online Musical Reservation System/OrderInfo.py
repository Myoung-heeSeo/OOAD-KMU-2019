import PersonalInfo

class OrderInfo:
    def __init__(self):
        self.id = 0
        self.personal = PersonalInfo.PersonalInfo()
        self.mid = 0
        self.seatNo = 0
        self.eticket = 0
        self.price = ''

    def getOrderInfo(self,id):
        f=open('Order.txt', 'r')
        for line in f:
            data=line.split(',')
            if int(data[0])==id:
                self.id = int(id)
                self.personal.getCustomer(data[1])
                self.mid=int(data[2])
                self.seatNo=int(data[3])
                self.eticket = int(data[4])
                self.price = data[5]



    def setOrderInfo(self, id, name, mid, sno, eticket, price):
        self.id=int(id)
        self.personal.getCustomer(name)
        self.mid=int(mid)
        self.seatNo = int(sno)
        self.eticket = int(eticket)
        self.price = price
        f= open("Order.txt", 'a')
        f.write('\n'+str(id)+', '+name+', '+str(mid)+', '+str(sno)+', '+str(eticket)+', '+price)
        f.close()
