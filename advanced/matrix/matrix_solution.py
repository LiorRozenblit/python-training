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
        tupleOfSelf = self.tuples()
        tupleOfOther = other.tuples()
        for i in range(len(tupleOfSelf[1])):
            for j in range(len(tupleOfSelf[1])):
                add.append(tupleOfSelf[i][j] + tupleOfOther[i][j])
            add2.append(tuple(add))
            add = []
        return 'Matrix({})'.format(tuple(add2))

    def __sub__(self, other):
        sub = []
        sub2 = []
        tupleOfSelf = self.tuples()
        tupleOfOther = other.tuples()
        for i in range(len(tupleOfSelf[1])):
            for j in range(len(tupleOfSelf[1])):
                sub.append(tupleOfSelf[i][j] - tupleOfOther[i][j])
            sub2.append(tuple(sub))
            sub = []
        return 'Matrix({})'.format(tuple(sub2))

    def __truediv__(self, other):
        div = []
        div2 = []
        tupleOfSelf = self.tuples()
        for i in range(len(tupleOfSelf[1])):
            for j in range(len(tupleOfSelf[1])):
                div.append(tupleOfSelf[i][j] * (1 / other))
            div2.append(tuple(div))
            div = []
        return 'Matrix({})'.format(tuple(div2))

    def __mul__(self, other):
        mul = []
        mul2 = []
        mul3 = []
        sum = 0
        if (type(self)) == int:
                x = other.tuples()
                for i in range(len(x[1])):
                    for j in range(len(x[1])):
                        for k in range(self):
                            sum += x[i][j]
                        mul2.append(sum)
                        sum = 0
                    mul.append(tuple(mul2))
                    mul2 = []
        if (type(other)) == int:
                y = self.tuples()
                for i in range(len(y[1])):
                    for j in range(len(y[1])):
                        for k in range(other):
                            sum += y[i][j]
                        mul2.append(sum)
                        sum = 0
                    mul.append(tuple(mul2))
                    mul2 = []
        else:
            y = self.tuples()
            x = other.tuples()
            for r in range(len(y[1])):
                mul3.append(0)
            for t in range(len(y[1])):
                mul2.append(mul3)
            for i in range(len(y[1])):
                for j in range(len(y[1])):
                    for k in range(len(y[1])):
                        mul2[i][j] += (y[i][k] * x[k][j])
                mul.append(tuple(mul2[i]))
                mul2 = []
                mul3 = []
                for r in range(len(y[1])):
                    mul3.append(0)
                for s in range(len(y[1])):
                    mul2.append(mul3)
        return 'Matrix({})'.format(tuple(mul))

    def __eq__(self, other):
        tupleOfSelf = self.tuples()
        tupleOfOther = other.tuples()
        return tupleOfOther == tupleOfSelf

    def __ne__(self, other):
        tupleOfSelf = self.tuples()
        tupleOfOther = other.tuples()
        return not tupleOfOther == tupleOfSelf

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        try:
            if self.__currentMatrix[self.count] in self.__currentMatrix:
                self.count += 1
                return self.__currentMatrix[self.count - 1]
        except:
            raise StopIteration

    def __hash__(self):
        return hash(str(self))









