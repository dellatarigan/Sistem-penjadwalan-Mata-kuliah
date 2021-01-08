class Module:
    def __init__(self, token, name, dosens):
        self._token = token
        self._name = name
        self._dosens = dosens

    def get_number(self): return self._token

    def get_name(self): return self._name

    def get_dosens(self): return self._dosens

    def __str__(self): return self._name
