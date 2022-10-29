from tkinter import N
import pandas as pd
import numpy as np

def cal_week(start,end):
    start,end=int(start),int(end)
    num_week=[]
    for i in range(1,21):
        if i>=start and i<=end:
            num_week.append(1)
        else:
            num_week.append(0)
    return num_week 

class table():
    def __init__(self):
        self.data={
            "classname":['demo'],
            "day":None,
            "time":None,
            "position":None,
            "week1":None,"week2":None,"week3":None,"week4":None,"week5":None,"week6":None,"week7":None,"week8":None,"week9":None,"week10":None,"week11":None,"week12":None,"week13":None,"week14":None,
            "week15":None,"week16":None,"week17":None,"week18":None,"week19":None,"week20":None,
        }
        self.classtable=pd.DataFrame(self.data)

    def add_class(self,name,day,time,positon,start,end):
        weeks=cal_week(start,end)
        addlist=[name,day,time,positon]+weeks
        print(addlist)
        if self.classtable.loc[0,"classname"]=='demo':
            self.classtable.loc[len(self.classtable)-1]=addlist
        else:
            self.classtable.loc[len(self.classtable)]=addlist

    def save(self):
        self.classtable.to_csv('class.csv')

a=table()
a.add_class('新中特',[1,3],[4],'西十二教N212',2,10)
a.add_class('人工智能导论',[1,3],[6],'西十二教N303',2,5)
a.add_class('学术规范与论文写作',[2,4],,'西十二教S212',11,16)
a.add_class('数理统计',[2,4],'西十二教N304',2,13)
a.add_class('机器人学',[2,6],'西十二教N303',2,5)
a.add_class('人工智能导论',[1,6],'西十二教N303',2,5)


a.save()

