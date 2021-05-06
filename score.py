import sqlite3

from PyQt5.QtWidgets import QDialog
from ui.ui_score import Ui_Dialog


class Score(QDialog, Ui_Dialog):

    EASY = 1
    MEDIUM = 2
    PRO = 3

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.con = sqlite3.connect("db/score.db")
        self.cursor = self.con.cursor()

        score = self.getMaxScore()

        self.easyLabel.setText(str(score[self.EASY]))
        self.mediumLabel.setText(str(score[self.MEDIUM]))
        self.proLabel.setText(str(score[self.PRO]))

    def getMaxScore(self):
        query = self.cursor.execute("""SELECT level, seconds FROM time""").fetchall()

        res = {self.EASY: 999,
               self.MEDIUM: 999,
               self.PRO: 999}

        for item in query:
            if item[0] == 'easy':
                res[self.EASY] = item[1]
            elif item[0] == 'medium':
                res[self.MEDIUM] = item[1]
            elif item[0] == 'pro':
                res[self.PRO] = item[1]
            else:
                continue
        return res

    def setMaxScore(self, level, score):
        if level == self.EASY:
            query_level = "easy"
        elif level == self.MEDIUM:
            query_level = "medium"
        elif level == self.PRO:
            query_level = "pro"
        else:
            return False

        query = self.cursor.execute(f"SELECT seconds FROM time WHERE level='{query_level}'").fetchone()

        if not query:
            max_score = 999
        else:
            max_score = query[0]

        if max_score < score:
             return

        query = self.cursor.execute(f"UPDATE time SET seconds={score} WHERE level='{query_level}'")
        self.con.commit()
