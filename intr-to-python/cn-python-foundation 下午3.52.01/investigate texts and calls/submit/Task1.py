"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# def count_number(textfile,callfile):
#     target= set()
#     for ele1 in textfile:
#         target.add(ele1[0])
#         target.add(ele1[1])
#     for ele2 in callfile:
#         target.add(ele2[0])
#         target.add(ele2[1])
#     return len(target)
target= set()
for ele1 in texts:
    target.add(ele1[0])
    target.add(ele1[1])
for ele2 in calls:
    target.add(ele2[0])
    target.add(ele2[1])

print("There are {} different telephone numbers in the records.".format(len(target)))

"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""
