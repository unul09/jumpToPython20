# 10

class Calculator:
    def __init__(self, numList):
        self.numList = numList

    def sum(self):
        result = sum(self.numList)
        return result

    def avg(self):
        result = sum(self.numList) / len(self.numList)
        return result


cal1 = Calculator([1, 2, 3, 4])
print(cal1.sum())
print(cal1.avg())