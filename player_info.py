players = []

class Player:

    def __init__(self, name, role, score):
        self.name = name
        self.role = role
        self.score = score
        players.append(self)

    def __str__(self):
        s = "Player name: {} , {} \n Player's role: {} ".format(self.name, self.role)
        return s

    def get_score(self):
        return self.score

print(players)
