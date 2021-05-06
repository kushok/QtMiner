class Field:
    BOMB = -1

    def __init__(self, height, width, bomb_num, first_step):
        assert width * height > bomb_num and first_step[1] * height + first_step[0] < width * height

        self.height = height
        self.width = width
        self.bn = bomb_num

        self.bombs = self.generateBombList(first_step)
        self.field = self.generateField()

    def generateBombList(self, first_step):
        # generating (x, y) bombs list
        from random import sample

        nums = list(range(self.width * self.height))
        nums.pop(first_step[1] * self.height + first_step[0])

        return [(n % self.height, n // self.height) for n in sample(nums, self.bn)]

    def generateField(self):
        field = []

        for _ in range(self.height):
            field.append([0] * self.width)

        for x, y in self.bombs:
            for a, b in self.getNearByPoints(x, y):
                field[a][b] += 1

        for x, y in self.bombs:
            field[x][y] = self.BOMB
        return field

    def getNearByPoints(self, x, y):
        points = []

        if y > 0:
            points.append((x, y - 1))
        if y < self.width - 1:
            points.append((x, y + 1))

        if x > 0:
            points.append((x - 1, y))
            if y > 0:
                points.append((x - 1, y - 1))
            if y < self.width - 1:
                points.append((x - 1, y + 1))

        if x < self.height - 1:
            points.append((x + 1, y))
            if y > 0:
                points.append((x + 1, y - 1))
            if y < self.width - 1:
                points.append((x + 1, y + 1))

        return points

    def __repr__(self):
        s = ""
        for i in range(self.height):
            for j in range(self.width):
                s += ("⛔" if self.field[i][j] == self.BOMB else str(self.field[i][j])) + " "
            s += "\n"
        return s

    def __str__(self):
        return self.__repr__()

    def getValue(self, x, y):
        assert 0 <= x < self.height and 0 <= y < self.width
        return self.field[x][y]

    def getBombs(self):
        return self.bombs
