class Seat:
    def __init__(self):
        self.mid = 0
        self.num = 0
        self.price = ''
        self.available = 0
        self.isSold = list()

    def getSeatInfo(self, mid):
        seatfile = open("Seat.txt", 'r')
        for line in seatfile:
            SeatList = line.split(',')
            if mid == int(SeatList[0]):
                self.mid = int(SeatList[0])
                self.num = int(SeatList[1])
                self.price = SeatList[2]
                self.available = int(SeatList[3])
                self.isSold = SeatList[4].split()
        seatfile.close()


    def changeSeatStatus(self, sno):
        self.getSeatInfo(self.mid)
        if self.isSold[sno] == '0':
            self.isSold[sno]='1'
            self.available-=1
        else:
            self.isSold[sno]='0'
            self.available+=1

        seatfile = open("Seat.txt", 'r')
        seattxt=''
        for line in seatfile:
            SeatList=line.split(',')
            if self.mid == int(SeatList[0]):
                seattxt = seattxt + str(self.mid) + ', ' + str(self.num) + ',' + self.price + ', ' + str(self.available)+', '+' '.join(
                    [i for i in self.isSold]) + "\n"
            else: seattxt+=line
        seatfile.close()
        seatfile= open("Seat.txt", 'w')
        for line in seattxt:
            seatfile.write(line)


        seatfile.close()

        print("Now The seat is available!") if self.isSold[sno] == '0' else print("The seat has been booked!")

    def setSeatsOfMusical(self, mid, numseats, price):
        self.mid = mid
        self.num = numseats
        self.price = price
        self.available = numseats
        self.isSold = [0] * int(numseats)



