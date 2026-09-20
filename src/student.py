class Student:
    def __init__(self, math, reading, writing):
        self.math = math
        self.reading = reading
        self.writing = writing

    def average_score(self):
        return (self.math + self.reading + self.writing) / 3

    def pass_or_fail(self):
        if self.average_score() >= 40:
            return "Pass"
        else:
            return "Fail"