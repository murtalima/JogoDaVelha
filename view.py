import numpy as np
import cv2
def img_map_creator(resolution):
    x,y =resolution
    img_map = np.zeros([y, x, 3], dtype=np.uint8)
    img_map.fill(255)
    img_map = cv2.line(img_map,(int(x/3)*1,0),(int(x/3)*1,y),[0,0,0],2)
    img_map = cv2.line(img_map,(int(x/3)*2,0),(int(x/3)*2,y),[0,0,0],2)
    img_map = cv2.line(img_map,(0,int(y/3)*1),(x,int(y/3)*1),[0,0,0],2)
    img_map = cv2.line(img_map,(0,int(y/3)*2),(x,int(y/3)*2),[0,0,0],2)
    return img_map
def refresh_map(img_map,map):
    y,x,_ = img_map.shape
    pos =[(int(x/6),int(y/6)) ,(int(3*x/6),int(y/6)), (int(5*x/6),int(y/6)), (int(x/6),int(3*y/6)), (int(3*x/6),int(3*y/6)), (int(5*x/6),int(3*y/6)), (int(x/6),int(5*y/6)), (int(3*x/6),int(5*y/6)), (int(5*x/6),int(5*y/6))]
    for x in range(len(map.map)):
        if(map.map[x]!=0):
            img_map = cv2.putText(img_map,map.map[x],pos[x],cv2.FONT_HERSHEY_COMPLEX,1,[0,0,0],1)

