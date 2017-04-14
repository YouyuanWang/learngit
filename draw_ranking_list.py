#!/usr/bin/env python
# coding:utf-8
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#读取信息
data = []
with open('list.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        data.append(line)
#print data

# 学术大牛相关信息
author = data[-50:-30]
author_name = []
author_IF = []
for i in author:
    author_name.append(filter(lambda x: not x.isdigit(), i))
    author_IF.append(filter(lambda x:  x.isdigit(), i))
#去掉空白字符
new = []
for i in author_IF :
    if i:
        new.append(int(i))
author_IF = new
new = []
for i in author_name :
    if i:
        new.append(i)
author_name = new

# 学术机构相关信息
unit = data[-20:]
unit_name = []
unit_IF = []
for i in unit:
    unit_name.append(filter(lambda x: not x.isdigit(), i))
    unit_IF.append(filter(lambda x:  x.isdigit(), i))
#去掉空白字符
new = []
for i in unit_IF :
    if i:
        new.append(int(i))
unit_IF = new
new = []
for i in unit_name :
    if i:
        if len(i)<30:    # 限制字符在30个以内
            new.append(i)
        else :
            j = i[0:30]
            new.append(j)
unit_name = new
#print  author_name
#print author_IF

# 数据可视化
def data_plot(data):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    max_value = max(data[1])
    data_len = len(data[1])
    rec_height = 1.0 / data_len
    for i in range(data_len):
        rec_width = data[1][i]
        r = 1.0 - rec_width*1.0/(max_value)*0.7
        g = 1.0 - rec_width*1.0/(max_value)*0.3
        b = 1.0 - rec_width*1.0/(max_value)*0.7
        patch = patches.Rectangle(
                (0,i*rec_height+rec_height*0.2),
                rec_width,
                rec_height*0.6,
                color=(r,g,b))
        ax.text(rec_width+0.1, i*rec_height+rec_height*0.4, data[0][i])
        ax.add_patch(patch)
    xtic = []
    ytic = []
    for i in range(max_value+6):
        xtic.append(i)
    for i in range(data_len):
        ytic.append(i*rec_height+rec_height*0.5)
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks(xtic)
    ax.yaxis.set_ticks(ytic)
    rank =range(1,11)
    ax.yaxis.set_ticklabels(rank,fontsize=13,color='r')
    #ax.yaxis.set_ticklabels(data[0])
    ax.set_xticks([])
    plt.xlabel('Impact Factor', fontsize=13,color='b')
    plt.title('Ranking List', fontsize=15, color='r')
    #plt.show()
data_plot((unit_name, unit_IF))
plt.savefig('unit_rank.png')
data_plot((author_name, author_IF))
plt.savefig('author_rank.png')
print 'the figure is saved!'