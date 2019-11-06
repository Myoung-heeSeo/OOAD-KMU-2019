import Musical
import Seat
import AdminMode
import BookTicket
import CheckMyTicket

class Website:
    def init__(self):
        self.musicalList = list()

    def start(self):
        print("=" * 88)
        print(" " * 36 + "Musical Schedule" + " " * 36)
        print("=" * 88)
        print("ID" + '  ' + "Musical Name" + ' ' * 19 + "Date" + ' ' * 12 + "Time" + ' ' * 3 + "Theatre" + ' ' * 24)
        print("=" * 3 + ' ' + "=" * 30 + ' ' + "=" * 15 + ' ' + "=" * 6 + ' ' + "=" * 30 + ' ')
        musicalfile = open("Musical.txt", 'r')
        for OneOfMusical in musicalfile:
            mlist = OneOfMusical.split(',')
            print(mlist[0] + ' ' * (3 - len(mlist[0])) + mlist[1] + ' ' * (31 - len(mlist[1])) + mlist[2] + ' ' * (
                    16 - len(mlist[2]))
                  + mlist[3] + ' ' * (7 - len(mlist[3])) + mlist[4] + ' ' * (30 - len(mlist[4])))
        musicalfile.close()
        print("=" * 88)
        print()
        print(">> Enter the musical ID you want to book or 0 to other options")
        option1 = (int(input()))
        print()
        if option1 == 0:
            while (True):
                print(">> Enter the option number you want to access")
                print("1: CheckMyTicket")
                print("2: AdminMode")
                print("3: Back to Home")
                option2 = int(input())
                if option2 == 1:
                    self.checkMyTicket()
                elif option2 == 2:
                    self.adminMode()
                elif option2 == 3:
                    self.start()
                else:
                    continue
                break
        else:
            self.selectMusical(option1)


    def selectMusical(self, id):
        book = BookTicket.BookTicket(id, self)



    def checkMyTicket(self):
        checkT = CheckMyTicket.CheckMyTicket()
        checkT.checkPersonalInfo(self)


    def adminMode(self):
        print(">> Admin LogIn")
        code = input("Admin Code:")
        admin = AdminMode.AdminMode()
        admin.adminLogin(code, self)

