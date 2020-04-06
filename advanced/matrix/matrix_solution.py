class Matrix:
    def __init__(self, x):
        self.__currentMatrix = x

    def unity(self):
        count = 0
        onlyOne = []
        unity = []
        for i in range(self):
            while len(onlyOne) < self:
                onlyOne.append(0)
            onlyOne[count] = 1
            count += 1
            unity.append(tuple(onlyOne))
            onlyOne = []
        return tuple(unity)


    def ones(self):
        z = []
        y = []
        for i in range(self):
            while len(y) < self:
                y.append(1)
            z.append(tuple(y))
        return tuple(z)


print(Matrix.unity(4))
print(Matrix.ones(3))
