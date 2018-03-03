import json
import numpy as np

# track_file = open("track.txt", 'wb')
# json_path = "results.json"
# with open("results.json", "r") as load_f:
#     load_dict = json.load(load_f)
#     # print(load_dict['results'])
#     # print type(load_dict)
#     num = 0
#     print len(load_dict['results'])
#     # print load_dict['results'][0]
#     for i in load_dict['results']:
#         track_file.write(str(num))
#         # if num < 3:
#         #     print i
#         # else:
#         #     break
#         num += 1
#         length = len(i.keys())
#         track_file.write(' '+str(length)+' ')
#         for id in xrange(length):
#             key = "track_{}".format(id)
#             # print key
#             # print i[key]
#             # print len(i[key])
#             length1 = len(i[key])
#             # if length1 != 10:
#             #     print "aha"
#             for k in xrange(length1):
#                 track_file.write(str(i[key][k]['camera'])+' '+str(i[key][k]['left'])+' '+str(i[key][k]['top'])+' '+str(i[key][k]['right'])+' '+str(i[key][k]['bottom'])+' ')
#                 # print i[key][k]['right']
#         track_file.write('\n')

txt_file = open('track.txt')
multi_monitor_txt = open("miltiMonitor.txt","wb")
for i in xrange(268):
    line = txt_file.readline()
    line1 = line.strip()
    line1 = line1.split(" ")
    print line1
    track_num = int(line1[1])
    print track_num
    camera_flag = np.zeros([3])

    for j in xrange(track_num*10):
        camera_flag[int(line1[2+j*5])] = 1
    camera_num = 0
    for j in xrange(3):
        if camera_flag[j] == 1:
            camera_num += 1
    print camera_num
    if camera_num != 1:
        print "hahaha ", i, camera_num
        multi_monitor_txt.write(line)
