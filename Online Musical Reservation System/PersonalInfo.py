class PersonalInfo:
    def __init__(self):
        self.name = ''
        self.phoneNum = ''

    def getCustomer(self, name):
        f= open("Person.txt", 'r')
        for line in f:
            data= line.split(',')
            if data[0]==name:
                self.name = data[0]
                self.phoneNum= data[1]
        f.close()
        if self.name=='':
            print("Can't find your History")
            return False

    def setCustomer(self, name, phoneNum):
        f= open("Person.txt", 'a')
        f.write(name+', '+phoneNum)
        f.close()
