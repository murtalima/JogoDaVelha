def game_status(map):
    winner = 0
    win_conditions = [[0, 4, 8],
                      [2, 4, 6],
                      [0, 3, 6],
                      [1, 4, 7],
                      [2, 5, 8],
                      [0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8]]
    for cond in win_conditions:
        if (map[cond[0]] != 0 and map[cond[0]] == map[cond[1]] and map[cond[1]] == map[
            cond[2]]):
            winner = map[cond[0]]
    if (0 not in map and winner == 0):
        winner = -1
    return winner
def play(map):
    result = {
    }
    r = replace_zeros(map,"IA")
    for x in range(len(r)):
        result[x]=0
        s = replace_zeros(r[x],"X")
        for y in range(len(s)):
            if(game_status(s[y])==0):
                result[x] +=1
            elif(game_status(s[y])=="IA"):
                result[x] +=8
            else:
                result[x] -= 10
    print(result)
    big_val = -1000
    big_num = -1000
    for x in result:
        if(result[x] > big_val):
            big_num = x
            big_val = result[x]
    try:
        res = r[big_num]
        try:

            for x in range(len(res)):
                if(str(res[x])!= str(map[x])):
                    print(x)
                    res = x
            return res
        except:
            return res
    except:
        print("error")

def replace_zeros (map,val):
    r = []
    for x in range(len(map)):
        if(map[x] == 0):
            nmap = map.copy()
            nmap[x] = val
            r.append(nmap)
    return r