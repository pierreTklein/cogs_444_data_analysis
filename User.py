from Entry import Entry

class User:
    def __init__(self, uid: AnyStr, entries: List[Entry]):
        self.uid = uid
        self.entries = entries

    def __str__(self):
        string = ""
        for e in self.entries:
            string = string + "\n" + e.__str__()
        return string
