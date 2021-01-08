class Lecture:
    def __init__(self, id, course, module, meeting_time):
        self._meeting_time = meeting_time
        self._id = id
        self._course = course
        self._module = module
        self._dosen = None
        self._meetingTime = None
        self._room = None

    def get_id(self): return self._id

    def get_course(self): return self._course

    def get_module(self): return self._module

    def get_dosen(self): return self._dosen

    def get_meeting_time(self): return self._meeting_time

    def get_room(self): return self._room

    def set_dosen(self, dosen): self._dosen = dosen

    def set_room(self, room): self._room = room

    def __str__(self):
        return str(self._course.get_name()) + ", " \
               + str(self._module.get_number()) + ", " \
               + str(self._room.get_number()) + ", " \
               + str(self._dosen.get_id()) + ", " \
               + str(self._meeting_time.get_id())
