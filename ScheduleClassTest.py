import numpy as np
class DailySchedule:
    def __init__(self,detailedSchedule = ['','','','7-1Ind & Soc','10-1 Ind & Soc']):

        #Create numpy array of length 6
        self.binarySchedule = np.array([1,1,1,1,1,1])

        #Go through detailed Schedule, update periodSchedule, 1 = free, 0 = busy

        index = 0 #Index for periodSchedule
        for scheduleItem in detailedSchedule:
            #if it is empty, change corresponding index to 1
            if scheduleItem != '':
                self.binarySchedule[index] = 0
            index = index + 1

        print(self.binarySchedule)
    def getBinarySchedule (self):
        return self.binarySchedule

class Person:
    def __init__(self, fullName, fullSchedule):
        self.fullName = fullName

        # Create schedule as an empty list
        self.schedule = []

        #loop through each day in fullSchedule
        for day in fullSchedule:

            #Create new DailySchedule and add to list
            curDaySched = DailySchedule(day)
            self.schedule.append(curDaySched)

        print(self.schedule)

#np.multiply(detailedSchedule, detailedSchedule2)

#print(Person1)
p1 = Person("Dean", [['', '', '', '7-1 Ind & Soc', '10-1 Ind & Soc'],
['11 Econ A SL/HL', '', '', '12 Econ SL'],
['10-1 Ind & Soc', '', '11 Econ A SL/HL', '', '7-1 Ind & Soc'],
['12 Econ SL', '', '', '', '10-1 Ind & Soc'],
['11 Econ A SL/HL', '', '7-1 Ind & Soc'],
['', '12 Econ SL', 'Ind & Soc Meeting', '', '11 Econ A SL/HL']])

p2 = Person("Brooke", [['10-1 English', '', '10-2 English', '12 English SL', '11 English SL'],
['', '', '10-1 English'],
['10-2 English', '11 English SL', 'English Meeting', '', '12 English SL'],
['10-1 English', '', '', '', '10-2 English'],
['', '', '', '10-2 English', '11 English SL'],
['', '', '', '10-1 English', '12 English SL']])

BinarySched1 = p1.schedule[0].getBinarySchedule()
BinarySched2 = p2.schedule[0].getBinarySchedule()

print (np.multiply(BinarySched1, BinarySched2))












#testSched = DailySchedule()








