from Field import Field


class Game:

    WIN = 1
    CONTINUE = 0
    LOSE = -1

    def __init__(self, height, width, bomb_num):
        self.height = height
        self.width = width
        self.bn = bomb_num
        # self.base_field = []
        self.points_to_open = set()

        self.game_field = []
        for _ in range(height):
            self.game_field.append(["▣"] * width)

        self.first_step = True
        self.opened_count = 0

    def doStep(self, x, y):
        if self.isFlagged(x, y):
            return self.CONTINUE

        if self.first_step:
            self.base_field = Field(self.height, self.width, self.bn, (x, y))
            self.first_step = False

        value = self.base_field.getValue(x, y)

        if value == Field.BOMB:
            bombs = self.base_field.getBombs()
            for a, b in bombs:
                self.game_field[a][b] = "⛔"
            return self.LOSE

        self.points_to_open.clear()
        self.getOpenField(x, y)

        for x, y in self.points_to_open:
            self.game_field[x][y] = str(self.base_field.getValue(x, y))
            self.opened_count += 1

        # print(self.opened_count, self.width * self.height - self.bn)
        if self.opened_count >= self.width * self.height - self.bn:
            return self.WIN
        return self.CONTINUE

    def changeFlag(self, x, y):
        if self.isFlagged(x, y):
            self.game_field[x][y] = "▣"
            return

        if self.game_field[x][y] == "▣":
            self.game_field[x][y] = "🚩"

    def isFlagged(self, x, y):
        return self.game_field[x][y] == "🚩"

    def getOpenField(self, x, y):
        if (x, y) in self.points_to_open or self.game_field[x][y] != "▣":
            return

        self.points_to_open.add((x, y))

        if self.base_field.getValue(x, y) == 0:
            area = self.base_field.getNearByPoints(x, y)
            for x, y in area:
                self.getOpenField(x, y)

    def __repr__(self):
        s = ""
        for i in range(self.height):
            s += f"{i + 1}: "
            for j in range(self.width):
                s += (self.game_field[i][j]) + " "
            s += "\n"
        return s

    def __str__(self):
        return self.__repr__()

    def getGameField(self):
        return self.game_field

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def getSize(self):
        return self.height, self.width
