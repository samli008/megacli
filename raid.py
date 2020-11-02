#! /usr/bin/env python
# -*- coding: cp936 -*-
log = open(r"c:\netapp\\"+"raid.txt",'w')

raid=[]
for i in range(24):
  raid.append("64"+":"+str(i))

word=""
for i in range(len(raid)):
  word=word+(raid[i]+',')
word=word.strip(",")
print(word)
log.write("disk="+word+'\n')
log.write("read -p \"pls input vd size[100gb]: \" size"+'\n')
log.write("megacli -CfgLdadd -r6 [$disk] WB Direct -sz$size -strpsz128 -a0"+'\n')

log.close()
