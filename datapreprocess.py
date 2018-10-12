#-*- coding: UTF-8 -*- 
import re
import jieba
import pandas as pd

#保存文件函数
def savefile(savepath,content):
    fp = open(savepath,"a",encoding="utf-8")
    fp.write(content)
    fp.write("\n")
    fp.close()

#读取文件的函数
def readfile(path):
	fp = open(path,"r",encoding="utf-8")
	content = fp.readlines()   
	fp.close()
	return content

f = "rd_forum_doc.txt"             
f1 = "forum_newdata.txt"
content = readfile(f)

# 只保留中文的正则表达式
cop = re.compile("[^\u4e00-\u9fa5]")

lines_seen = set()
for line in content:
    string = cop.sub("", line)
    if string not in lines_seen:    #去除重复行，保留第一次出现的重复行
        savefile(f1,string)         
        lines_seen.add(string)

newcontent = readfile(f1)
my_dict1 = "./userdict/financial_complete.txt"
my_dict2 = "./userdict/P2P_Online_loan_platform_2017.txt"
my_dict3 = "./userdict/platform_name.txt"
my_dict4 = "./userdict/mydict.txt"
jieba.load_userdict(my_dict1)
jieba.load_userdict(my_dict2)
jieba.load_userdict(my_dict3)
jieba.load_userdict(my_dict4)
for line in newcontent:
	content_seg = jieba.cut(line)
	print('/'.join(content_seg))


