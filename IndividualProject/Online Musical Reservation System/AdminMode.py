# def adminLogin(AdminCode):
import Seat
import ManageMusicalObject
import ChangeSeat

class AdminMode:
    def __init__(self):
        self.code = ''
        self.approval = 0


    def adminLogin(self, code, website):
        adminfile = open("Admin.txt", 'r')
        for admincode in adminfile:
            if int(code) == int(admincode):
                self.code = code
                self.approval = 1
                self.getInst(website)
            else:
                continue
        if self.approval==0:
            print("Wrong admin code! Please enter the available code")
            website.adminMode()
        # adminfile.close()

    def getInst(self, website):
        print("Enter the option number you want to access")
        print("1: Manage Musical List")
        print("2: Change SeatStatus")
        print("3: Log Out")
        print()
        inst = int(input())
        if inst==1:
            print("Manage Musical List")
            MusicalObjectManager=ManageMusicalObject.ManageMusicalObject()
            MusicalObjectManager.displayMusicalList(website, self)
        elif inst==2:
            print("Chang SeatStatus")
            SeatManager=ChangeSeat.ChangeSeat(website, self)
        elif inst==3:
            self.adminLogout(website)
        else:
            self.getInst()


    # def changeSeat(self):

    def adminLogout(self, website):
        self.code = ''
        self.approval = 0
        website.start()




