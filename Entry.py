

class Entry:
    def __init__(self, uid: AnyStr, methodType: int, numHelped: int, crowd: int, completion: int, difficulty: int, comfort: int):
        self.uid = uid
        self.methodType = methodType
        self.numHelped = numHelped
        self.crowd = crowd
        self.completion = completion
        self.difficulty = difficulty
        self.comfort = comfort

    def __str__(self) -> str:
        return "{0},{1}:{2},{3},{4},{5},{6}".format(self.uid, self.methodType, self.numHelped, self.crowd, self.completion, self.difficulty, self.comfort)
