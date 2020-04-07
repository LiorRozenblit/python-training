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
        ones = []
        currentTuple = []
        for i in range(self):
            while len(currentTuple) < self:
                currentTuple.append(1)
            ones.append(tuple(currentTuple))
        return tuple(ones)

    def __str__(self):
        return '{}'.format(self.__currentMatrix)

    def __repr__(self):
        return 'Matrix({})'.format(self.__currentMatrix)

    def tuples(self):
        self.__currentMatrix = tuple(self.__currentMatrix)
        return self.__currentMatrix

    def __add__(self, other):
        add = []
        add2 = []
        y = self.tuples()
        if type(other) != tuple:
            x = other.tuples()
        else:
            x = other
        for i in range(len(y[1])):
            for j in range(len(y[1])):
                add.append(y[i][j] + x[i][j])
            add2.append(tuple(add))
            add = []
        return 'Matrix({})'.format(tuple(add2))


a = Matrix(((1, 2, 5), (3, 5, 4), (7, 9, 3)))
b = Matrix(((4, 2, 2), (9, 5, 1), (1, 2, 9)))
print(a + Matrix.unity(3))
print(b + Matrix.ones(3))


