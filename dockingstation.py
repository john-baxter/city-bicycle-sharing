class DockingStation():

    def __init__(self):
        self.bikes = []

    def dock(self, string):
        self.bikes.append(string)

    def release(self):
        bike = self.bikes.pop()
        return bike
        