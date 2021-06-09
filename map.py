class Map:
    def __init__(self):
        self.map =[0,0,0,0,0,0,0,0,0]
        self.plays = []
        self.winner = 0
    def play (self,player,pos):
        if(self.winner == 0):
            if not self.map[pos]:
                self.map[pos] = player
                self.plays.append([player,pos])
                self.game_status()
                return True
            else:
                return False
    def game_status (self):
        win_conditions =[[0,4,8],
                         [2,4,6],
                         [0,3,6],
                         [1,4,7],
                         [2,5,8],
                         [0,1,2],
                         [3,4,5],
                         [6,7,8]]
        for cond in win_conditions:
            if(self.map[cond[0]] != 0 and self.map[cond[0]] == self.map[cond[1]] and self.map[cond[1]] == self.map[cond[2]]):
                self.winner = self.map[cond[0]]
        if(0 not in self.map and self.winner == 0):
            self.winner = -1
    def view_map (self):
        for c in range(0,len(self.map),3):
            print(self.map[c],self.map[c+1],self.map[c+2])


