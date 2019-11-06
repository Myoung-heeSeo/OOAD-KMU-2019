import Seat

class ChangeSeat():
    def __init__(self, website, admin):
        self.MID = 0
        self.seatno = 0
        self.changeSeatStatus(website, admin)

    def getMID(self):
        print(">> Enter the musical ID to change Seat Status")
        self.MID=int(input())

    def getSeatNo(self):
        print(">> Enter the seat number to change Seat Status")
        self.seatno = int(input())

    def changeSeatStatus(self, website, admin):
        self.getMID()
        self.getSeatNo()
        seat = Seat.Seat()
        seat.getSeatInfo(self.MID)
        seat.changeSeatStatus(self.seatno)
        admin.getInst(website)