import cv2
import time
import view
import IA
import random
from map import Map
def keybord_pos (k):
    if k == 55:  # 7
        return 0
    if k == 56:  # 8
        return 1
    if k == 57:  # 9
        return 2
    if k == 52:  # 4
        return 3
    if k == 53:  # 5
        return 4
    if k == 54:  # 6
        return 5
    if k == 49:  # 1
        return 6
    if k == 50:  # 2
        return 7
    if k == 51:  # 3
        return 8
    if k == ord('r'):
        return 9
    return -1
def play(resolution, player1 , player2):
    map =Map()
    y,x = resolution
    last_time = time.time()
    img_map = view.img_map_creator(resolution)
    cc = 0
    Continue = True
    while(Continue):
        img = cv2.cvtColor(img_map, cv2.COLOR_RGB2BGR)
        img = cv2.putText(img,'FPS: {0:.2f}'.format((time.time()-last_time)*1000),(int(x*0.02),int(y*0.02)),cv2.FONT_HERSHEY_COMPLEX,0.3,[255,0,0],1)
        last_time = time.time()

        if(map.winner ==0):
            cv2.imshow('Tic Tac Toe', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            k = cv2.waitKey(15) & 0xFF
            pos = keybord_pos(k)
            if(pos !=-1):
                if(cc%2==0):
                    if(map.play(player1,pos)):
                        cc +=1
                else:
                    if (map.play(player2, pos)):
                        cc += 1
            img = view.refresh_map(img_map, map)
        else:
            if(map.winner!=-1):
                img = cv2.putText(img,(map.winner + " Win"),(0,int(y/2)),cv2.FONT_HERSHEY_COMPLEX,2,[0,255,0],2)
                print(map.plays)
            else:
                img = cv2.putText(img, ("It's a tie"), (0, int(y / 2)), cv2.FONT_HERSHEY_COMPLEX, 2,[0, 0, 255], 2)
            cv2.imshow('Tic Tac Toe', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            cv2.waitKey(0)
            map=Map()
            img_map = view.img_map_creator(resolution)

        if k == ord('q'):
            cv2.destroyAllWindows()
            break
def play_IA(resolution,who_first):
    map = Map()

    #map.play("IA",random.randint(0,8))
    y, x = resolution
    last_time = time.time()
    img_map = view.img_map_creator(resolution)
    cc = 0
    Continue = True
    while (Continue):

        img = cv2.cvtColor(img_map, cv2.COLOR_RGB2BGR)
        img = cv2.putText(img, 'FPS: {0:.2f}'.format((time.time() - last_time) * 1000), (int(x * 0.02), int(y * 0.02)),
                          cv2.FONT_HERSHEY_COMPLEX, 0.3, [255, 0, 0], 1)
        last_time = time.time()

        if (map.winner == 0):
            cv2.imshow('Tic Tac Toe', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            k = cv2.waitKey(15) & 0xFF
            pos = keybord_pos(k)
            if (pos != -1):
                map.play('X', pos)
                map.play("IA", IA.play(map.map))


            img = view.refresh_map(img_map, map)
        else:
            if (map.winner != -1):
                img = cv2.putText(img, (map.winner + " Win"), (0, int(y / 2)), cv2.FONT_HERSHEY_COMPLEX, 2, [0, 255, 0],
                                  2)
                print(map.plays)
            else:
                img = cv2.putText(img, ("It's a tie"), (0, int(y / 2)), cv2.FONT_HERSHEY_COMPLEX, 2, [0, 0, 255], 2)
            cv2.imshow('Tic Tac Toe', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            cv2.waitKey(0)
            map = Map()
            if (cc % 2 == 0):
                map.play("IA", random.randint(0, 8))
            cc +=1
            img_map = view.img_map_creator(resolution)

        if k == ord('q'):
            cv2.destroyAllWindows()
            break

resolution = (300,300)
play_IA(resolution,0)