from Course import Course
from Dosen import Dosen
from MeetingTime import MeetingTime
from Module import Module
from Room import Room


class Data:
    def __init__(self):
        rooms = [["GD923", 60], ["GD924", 60], ["GD926", 60], ["GD929", 60], ["GD933", 60]]
        meeting_times = [
            ["1. Block", "08:00 – 09:50"],
            ["2. Block", "10:00 – 11:50"],
            ["3. Block", "13:00 – 14:50"],
            ["4. Block", "15:00 – 16:50"]
        ]
        dosens = [
            ["HTS", "Humasak Simanjuntak"],
            ["SGS", "Samuel Situmeang"],
            ["JUN", "Junita Amalia"],
            ["MSS", "Mario Simaremare"],
            ["THS", "Tennov Simanjuntak"],
            ["DWS", "Devis Wawan Saputra"],
            ["BLT", "Bonar Lumban Tobing"],
            ["IUS", "Iustisia Simbolon"],
            ["PAT", "Parmonangan Togatorop"],
            
        ]

        self._rooms = []
        self._meeting_times = []
        self._dosens = []
        self.fill_objects(rooms, meeting_times, dosens)

        module1 = Module("BASDATLAN", "Advanced Database",
                         [self.get_dosen("HTS")])
        module2 = Module("CERTAN", "Artificial Intelligence",
                         [self.get_dosen("SGS")])
        module3 = Module("PROBSTAT", "Probability and Statistics",
                         [self.get_dosen("JUN"), self.get_dosen("THS")])
        module4 = Module("PPW", "Web Application Programming and Testing",
                         [self.get_dosen("MSS")])
        module5 = Module("ALSTRUDAT", "Algorithms and Data Structures",
                         [self.get_dosen("THS"), self.get_dosen("HTS"), self.get_dosen("PAT"), self.get_dosen("SGS")])
        module6 = Module("TEKNO", "Technopreneurship",
                         [self.get_dosen("DWS")])
        module7 = Module("ATI", "Religion and Ethics",
                         [self.get_dosen("BLT")])
        module8 = Module("RPL", "Software Engineering",
                         [self.get_dosen("IUS")])
        module9 = Module("MPSI", "Information System Project Management",
                         [self.get_dosen("PAT")])
        self._modules = [module1, module2, module3, module4, module5, module6]

        course1 = Course("11SI", [module1, module3, module4, module7], 59)
        course2 = Course("12SI", [module2, module4, module5, module8], 50)
        course3 = Course("13SI", [module4, module5, module6, module9], 56)
        course4 = Course("14SI", [module5, module3, module1, module9], 48)
        self._courses = [course1, course2, course3, course4]

    def get_dosens(self):
        return self._dosens

    def get_rooms(self):
        return self._rooms

    def get_modules(self):
        return self._modules

    def get_courses(self):
        return self._courses

    def get_meeting_times(self):
        return self._meeting_times

    def fill_objects(self, rooms, meeting_times, dosens):
        for i in range(0, len(rooms)):
            self._rooms.append(Room(rooms[i][0], rooms[i][1]))
        for i in range(0, len(meeting_times)):
            self._meeting_times.append(MeetingTime(meeting_times[i][0], meeting_times[i][1]))
        for i in range(0, len(dosens)):
            self._dosens.append(Dosen(dosens[i][0], dosens[i][1]))

    def get_dosen(self, name):
        return next((dosen for dosen in self._dosens if dosen.get_id() == name), None)
