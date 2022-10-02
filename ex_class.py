class Angle:
    def __init__(self, value):
        self.degrees = value % 360

    def is_acute(self):
        if self.degrees < 90:
            return True
        else:
            return False

    def add(self, other):
        return Angle(self.degrees + other.degrees)
