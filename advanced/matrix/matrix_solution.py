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
        return Matrix(tuple(unity))

    def ones(self):
        ones = []
        currentTuple = []
        for i in range(self):
            while len(currentTuple) < self:
                currentTuple.append(1)
            ones.append(tuple(currentTuple))
        return Matrix(tuple(ones))

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
        x = other.tuples()
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
        x = other.tuples()
        for i in range(len(y[1])):
            for j in range(len(y[1])):
                add.append(y[i][j] - x[i][j])
            add2.append(tuple(add))
            add = []
        return 'Matrix({})'.format(tuple(add2))

    def __truediv__(self, other):
        add = []
        add2 = []
        y = self.tuples()
        x = other
        for i in range(len(y[1])):
            for j in range(len(y[1])):
                add.append(y[i][j] * (1 / x))
            add2.append(tuple(add))
            add = []
        return 'Matrix({})'.format(tuple(add2))

    def __mul__(self, other):
        add2 = []
        add3 = []
        add4 = []
        sum = 0
        if (type(self)) == int:
                x = other.tuples()
                for i in range(len(x[1])):
                    for j in range(len(x[1])):
                        for k in range(self):
                            sum += x[i][j]
                        add3.append(sum)
                        sum = 0
                    add2.append(tuple(add3))
                    add3 = []
        if (type(other)) == int:
                y = self.tuples()
                for i in range(len(y[1])):
                    for j in range(len(y[1])):
                        for k in range(other):
                            sum += y[i][j]
                        add3.append(sum)
                        sum = 0
                    add2.append(tuple(add3))
                    add3 = []
        else:
            y = self.tuples()
            x = other.tuples()
            for r in range(len(y[1])):
                add4.append(0)
            for t in range(len(y[1])):
                add3.append(add4)
            for i in range(len(y[1])):
                for j in range(len(y[1])):
                    for k in range(len(y[1])):
                        add3[i][j] += (y[i][k] * x[k][j])
                add2.append(tuple(add3[i]))
                add3 = []
                add4 = []
                for r in range(len(y[1])):
                    add4.append(0)
                for s in range(len(y[1])):
                    add3.append(add4)
        return 'Matrix({})'.format(tuple(add2))

    def __eq__(self, other):
        y = self.tuples()
        x = other.tuples()
        if x == y:
            return True
        return False

    def __ne__(self, other):
        y = self.tuples()
        x = other.tuples()
        if x == y:
            return False
        return True


a = Matrix(((1, 2, 5), (3, 5, 4), (7, 9, 3)))
b = Matrix(((4, 2, 2), (9, 5, 1), (1, 2, 9)))
print(b * 5)
print(b * a)
print(a / 3)
for line in a:
    print(line)




