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
        tuples = tuple(self.__currentMatrix)
        return tuples

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

    def __sub__(self, other):
        add = []
        add2 = []
        y = self.tuples()
        if type(other) != tuple:
            x = other.tuples()
        else:
            x = other
        for i in range(len(y[1])):
            for j in range(len(y[1])):
                add.append(y[i][j] - x[i][j])
            add2.append(tuple(add))
            add = []
        return 'Matrix({})'.format(tuple(add2))

    def __mul__(self, other):
        add2 = []
        add3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        y = self.tuples()
        if type(other) != tuple:
            x = other.tuples()
        else:
            x = other
        for i in range(len(y[1])):
            for j in range(len(y[1])):
                for k in range(len(y[1])):
                    add3[i][j] += (y[i][k] * x[k][j])
        add2.append(tuple(add3))
        return 'Matrix({})'.format(tuple(add2))

    def __eq__(self, other):
        y = self.tuples()
        if type(other) != tuple:
            x = other.tuples()
        else:
            x = other
        if x == y:
            return True
        return False

    def __ne__(self, other):
        y = self.tuples()
        if type(other) != tuple:
            x = other.tuples()
        else:
            x = other
        if x == y:
            return False
        return True


a = Matrix(((1, 2, 5), (3, 5, 4), (7, 9, 3)))
b = Matrix(((4, 2, 2), (9, 5, 1), (1, 2, 9)))
print(a + Matrix.unity(3))
print(b + Matrix.ones(3))
print(a + b)
print(a - b)
print(a - Matrix.unity(3))
print(b - Matrix.ones(3))
d = Matrix(((1, 2, 5), (3, 5, 4)))
c = Matrix(((1, 2, 5), (3, 5, 4)))
print(d == c)
print(d != c)
print(a * b)


