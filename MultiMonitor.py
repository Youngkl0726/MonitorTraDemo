from os import path
import numpy as np
from PIL import Image
from sklearn import linear_model
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def regression(cor_pic, cor_world):
    X = np.array(cor_pic)
    Z1 = []
    Z2 = []
    for i in xrange(4):
        Z1.append(cor_world[i][0])
    for i in xrange(4):
        Z2.append(cor_world[i][1])
    regr = linear_model.LinearRegression()

    regr.fit(X, Z1)
    a1, b1 = regr.coef_, regr.intercept_
    regr.fit(X, Z2)
    a2, b2 = regr.coef_, regr.intercept_
    return a1, b1, a2, b2

def drawTra(a, b):
    # print a,b
    txt_file = open("miltiMonitor.txt")
    sleep_t = 5.000

    for i in xrange(5):

        line = txt_file.readline()
        line = line.strip()
        line = line.split(" ")
        print line
        track_num = int(line[1])
        draw_x = []
        draw_y = []
        for j in xrange(track_num*10):
            camera_id = int(line[2+j*5])
            pic_x = (int(line[3+j*5])+int(line[5+j*5]))/2.0
            pic_y = int(line[6+j*5])
            a_1 = a[camera_id*2]
            a_2 = a[camera_id*2+1]
            b_1 = b[camera_id*2]
            b_2 = b[camera_id*2+1]
            # print a_1, a_2, b_1, b_2
            cor_pic = np.array([[pic_x, pic_y]])
            world_x = -1.0 * (np.sum(a_1 * cor_pic) + b_1)
            world_y = np.sum(a_2 * cor_pic) + b_2
            draw_x.append(world_x)
            draw_y.append(world_y)
        print("x len is: {}".format(len(draw_x)))
        fig1 = plt.figure(1)
        plt.pause(sleep_t)
        plt.clf()
        plt.axis([-170, 0, 0, 50])
        plt.scatter(draw_x[0:], draw_y[0:], c='blue')
    plt.show()

def main():
    cor_pic_0 = [[887, 1047], [1289, 753], [1096, 527], [1228, 369]]
    cor_world_0 = [[0, 0], [4, 2], [9, 1], [15, 2.1]]
    a1_0, b1_0, a2_0, b2_0 = regression(cor_pic_0, cor_world_0)
    # print a1_0

    cor_pic_1 = [[595, 535], [1324, 450], [479, 612], [1451, 482]]
    cor_world_1 = [[66, 18], [56, 22], [67, 14], [54, 20]]
    a1_1, b1_1, a2_1, b2_1 = regression(cor_pic_1, cor_world_1)
    # print a1_1

    cor_pic_2 = [[882, 514], [727, 564], [508, 670], [1080, 833]]
    cor_world_2 = [[146, 3], [150, 5], [153, 7], [156, 2]]
    a1_2, b1_2, a2_2, b2_2 = regression(cor_pic_2, cor_world_2)
    # print a1_2
    a = []
    b = []
    a.append(a1_0)
    a.append(a2_0)
    a.append(a1_1)
    a.append(a2_1)
    a.append(a1_2)
    a.append(a2_2)

    b.append(b1_0)
    b.append(b2_0)
    b.append(b1_1)
    b.append(b2_1)
    b.append(b1_2)
    b.append(b2_2)
    # print a, b
    drawTra(a, b)

if __name__ == '__main__':
    main()


