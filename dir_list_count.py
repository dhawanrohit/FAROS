import os
from os.path import join, isdir

if __name__ == "__main__":
    PATH_D = "c:/Users/347905/Downloads"
    dir_lst = []
    x,y = 0,0

    dir_lst = os.listdir(PATH_D)
    for i in range(0,len(dir_lst)-1):
        if os.path.isdir(PATH_D+"/"+dir_lst[i]):
            x = x+1
            for items in os.listdir(PATH_D+"/"+dir_lst[i]):
                dir_lst.append(PATH_D+"/"+dir_lst[i])
        else:
            y=y+1

    print(dir_lst, x, y)