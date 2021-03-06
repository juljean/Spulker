import datetime

class TimeContainer:
    def __init__(self, startDate, events):
        self.startDay = startDate
        self.events = events

    def initialize(self, numCells):
        pass

class CEvent:
    def __init__(self, startDate, endDate, person, tag):
        self.startDate = startDate
        self.endDate = endDate
        self.person = person
        self.tag = tag

class CDay(TimeContainer):
    def __init__(self, events, startDate):
        super().__init__(startDate, events)


class CWeek(TimeContainer):
    def __init__(self, events, startDate):
        super().__init__(startDate, events)
        self.sevenDays = []

    def splitEvents(self):
        sortedEvents = [[] for i in range(7)]
        for event in self.events:
            delta = datetime.timedelta(event.startDate - self.startDate).days
            sortedEvents[delta].append(event)
        return sortedEvents

    def initialize(self, numCells):
        sortedEvents = self.splitEvents()
        for i in range(numCells):
            self.sevenDays.append(CDay(sortedEvents[i], datetime.self.startDate + datetime.timedelta(days = i)))

class CMonth(TimeContainer):
    def __init__(self, events, startDate):
        super().__init__(startDate, events)


class CYear(TimeContainer):
    def __init__(self, events, startDate):
        super().__init__(startDate, events)

class CTag:
    def __init__(self, name):
        self.name = name

class CPerson:
    def __init__(self, id: int, photo,
                 birthdayDate: datetime.date,
                 phoneNumber, phoneNumberComment: str,
                 email: str, address: str,
                 relationshipLevel: int,
                 familyMember: CDay.CPerson,
                 ):
        self.id = id
        self.photo = photo


class CName:
    def __init__(self, name: str, surname: str, secondName: str):
        self.name = name
        self.surname = surname
        self.secondName = secondName

#make a height parameter

