# coding=utf-8
import pandas as pd
import numpy as np
import datetime
import os
import xlrd
import openpyxl
os.chdir("E:\姜林\其他\统计数据0219\拆借")
path=os.getcwd()
print(path)
filelist=[]
for root,dirs,files in os.walk(path):
    for file in files:
        if os.path.splitext(file)[1] == '.xls':
            filelist.append(file)

dflist=[]
for i in range(len(filelist)):

    dflist.append(pd.read_excel(filelist[i],shiprows=1))
data=pd.concat(dflist)
data.drop_duplicates('成交编号','first', inplace = True)
#print(data.head(20))
data["首次结算日"]=pd.to_datetime(data["首次结算日"],format="%Y/%m")
data["首次结算日"]=data["首次结算日"].apply(lambda x:datetime.datetime.strftime(x,"%Y%m"))
#print(data["首次结算日"].head(10))
df=data.groupby(["对手方","首次结算日"]).agg("sum")
print(df.head(10))
df.to_excel("E:\姜林\其他\统计数据0219\拆借\拆借统计2.xlsx" )
print(df.index)