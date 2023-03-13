class Result:

    def __init__(self, value, flow):
        self.value = value
        self.flow = flow

    def to_string(self):
        return f"{self.value} {self.flow}"
