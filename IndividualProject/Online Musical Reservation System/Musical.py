import Seat

class Musical:
    def __init__(self):
        self.id=''
        self.name=''
        self.date=''
        self.time=''
        self.theatre=''
        self.seat=''

    def getMusicalObject(self, id):
        musicalfile = open("Musical.txt", 'r')
        for line in musicalfile:
            MusicalList = line.split(',')
            if id == int(MusicalList[0]):
                self.id = MusicalList[0]
                self.name = MusicalList[1]
                self.date = MusicalList[2]
                self.time = MusicalList[3]
                self.theatre = MusicalList[4]
        musicalfile.close()
        s= Seat.Seat()
        s.getSeatInfo(id)
        self.seat = s

    def setMusicalObject(self, id, name, date, time, theatre, seats, price):
        self.id=id
        self.name=name
        self.date=date
        self.time=time
        self.theatre=theatre

        #setSeatsOfMusical
        s= Seat.Seat()
        s.setSeatsOfMusical(self.id, seats, price)
        self.seat=s

