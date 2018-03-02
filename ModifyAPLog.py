from os import path
import numpy as np
from PIL import Image
from sklearn import linear_model
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def get_ap_log(filename):
    file = open(filename)
    txt_file = open('ap.txt', 'wb')
    num = 0
    frame_id = 0
    for i in xrange(1821):
    # for i in xrange(10):
        print i
        line = file.readline()
        line = line.strip()
        line = line.split(" ")
        # print line
        if len(line) == 2:
            frame_id = line[1]
            # print "frame_id is : ", frame_id
        if len(line) > 2:
            # print line[5]
            line1 = line[5].split(',')
            # print frame_id, line[0], line1
            # print line1
            # print len(line1)
            txt_file.write(frame_id+' '+line[0])
            for j in xrange(28):
                txt_file.write(' '+line1[j])
            txt_file.write('\n')
    txt_file.close()

def get_ap_log1(filename):
    file = open(filename)
    res_line = [[] for i in xrange(1066)]
    for i in xrange(1066):
        # print i
        line = file.readline()
        line = line.strip()
        line = line.split(" ")
        # print len(line)
        # print line
        res_line[i].append(int(line[0]))
        res_line[i].append(int(line[1]))
        res_line[i].append(float(line[-4]))
        res_line[i].append(float(line[-3]))
        res_line[i].append(float(line[-2]))
        res_line[i].append(float(line[-1]))
    # print res_line
    return res_line

def drawTra(ap_res):
    cor_x = []
    cor_y = []
    cor_pic = [[595, 535], [1324, 450], [479, 612], [1451, 482]]
    cor_world = [[66, 18], [56, 22], [67, 14], [54, 20]]
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

    sleep_t = 0.001
    draw_x = []
    draw_y = []

    for i in xrange(1066):
        person_id = ap_res[i][1]
        pic_id = ap_res[i][0]
        point1_x = ap_res[i][2]
        point1_y = ap_res[i][3]
        point2_x = ap_res[i][4]
        point2_y = ap_res[i][5]
        mid_x = ((point1_x + point2_x) / 2.0)
        mid_y = ((point1_y + point2_y) / 2.0)
        mid_x = min(1920.0, mid_x)
        mid_y = min(1080.0, mid_y)
        print mid_x, mid_y
        # cor_pic = []
        # cor_pic.append(mid_x)
        # cor_pic.append(mid_y)
        cor_pic = np.array([[mid_x,mid_y]])
        # cor_pic = cor_pic.reshape([-1])
        # print cor_pic.shape
        # a_x = [[-0.01450711],[-0.0079112]]
        # a_x = np.array(a_x)
        # print a_x.shape
        # b_x = [78.8213134072]
        #
        # a_y = [[-0.00105179],[-0.05469549]]
        # a_y = np.array(a_y)
        # b_y = [47.9400658035]
        world_x = -1.0* (np.sum(a1*cor_pic)+b1)
        world_y = np.sum(a2*cor_pic)+b2
        print("i is: {}, person_id is: {}".format(i,person_id))
        print world_x, world_y
        draw_x.append(world_x)
        draw_y.append(world_y)
        fig1 = plt.figure(1)
        plt.pause(sleep_t)
        plt.clf()
        plt.axis([-80, 0, 0, 50])
        plt.scatter(draw_x[:], draw_y[:], c='blue', marker = 'o')
    plt.show()
    print draw_x

def main():
    # ap_file = r'AP.txt'
    # get_ap_log(ap_file)
    ap_res = get_ap_log1('ap.txt')
    drawTra(ap_res)

if __name__ == '__main__':
    main()

