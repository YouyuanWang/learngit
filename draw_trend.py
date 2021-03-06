#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt

paper_num = []
with open('year_papernumber.txt') as f:
    lines = f.readlines()
    for line in lines:
        num = filter(str.isdigit,line)
        paper_num.append(int(num))
year = range(1996,2016)
min_num = min(paper_num)
max_num = max(paper_num)
#print len(year),len(paper_num)
plt.plot(year,paper_num,'-')
plt.xlabel('Year(1996-2016)',fontsize=15)
plt.ylabel('Number of Paper(Conference,Patent) Published',fontsize=10)
plt.title('the Research Trend in nearly 20 years',fontsize=15,color='g')
plt.axis([1994,2017,min_num*0.95,max_num*1.05])
plt.savefig('ResearchTrend.png')
plt.show()



