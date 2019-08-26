import Musical

class ManageMusicalObject:
    def __init__(self):
        self.MID=0


    def displayMusicalList(self, website, admin):
        # display MusicalList
        print("=" * 88)
        print(" " * 34 + "Manage Musical List" + " " * 35)
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

        print(">> Enter the instruction below")
        print(" " * 4 + "add \"[musical_id], [musical_name], [date], [time], [theatre], [num_of_seats], [price]\"")
        print(" " * 4 + "delete [musical_id]")
        print(" " * 4 + "0: back to the admin option")
        print()
        inst=input()
        if(inst[:3]=="add"):
            self.addMusicalObject(inst[4:])

        elif (inst[:6]=="delete"):
            self.deleteMusicalObject(inst[7:])
        elif inst=='0':
            admin.getInst(website)
        else:
            print("Inavailable Instruction!")
        self.displayMusicalList(website, admin)


    def addMusicalObject(self, datastr):
        datastr=datastr.strip('"')
        data=datastr.split(",")
        musicalObj=Musical.Musical()
        musicalObj.setMusicalObject(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        seatObj=musicalObj.seat

        #append music object to "Musical.txt" file
        musicalfile = open("Musical.txt", 'a')
        datastr.replace('"','')
        musicalfile.write(datastr)
        musicalfile.close()

        #append seat object to "Seat.txt" file
        seatfile = open("Seat.txt", 'a')
        stxt='\n'+seatObj.mid + ',' + seatObj.num + ',' +seatObj.price + ',' + ' 0'*int(seatObj.num)
        seatfile.write(stxt.replace('"', ''))
        # seatfile.write('\n'+seatdata)
        seatfile.close()

        print("Successfully add musical object!")


    def deleteMusicalObject(self, id):
        #delete musicalObj from 'Musical.txt'
        f=open('Musical.txt', 'r')
        str=''
        for line in f:
            if (line[:len(id)]==id):
                continue
            else: str+=line
        f.close()
        f=open('Musical.txt', 'w')
        f.write(str)
        f.close()

        #delete seatObj from 'Seat.txt'
        f=open('Seat.txt', 'r')
        str=''
        for line in f:
            if(line[:len(id)]==id):
                continue
            else: str+=line
        f.close()
        f=open('Seat.txt', 'w')
        f.write(str)
        f.close()

        print("Successfully delete musical object!")

