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

def output_list(input_text,input_call):
    all_num_list = []
    i = 0
    j = 0
    x = 0
    y = 0
    while i < len(input_call):
        all_num_list.append(input_call[i][0])
        i += 1
    num_list = list(set(all_num_list))
    while j < len(input_call):
        if input_call[j][1] in num_list:
            num_list.remove(input_call[j][1])
        j += 1
    while x < len(input_text):
        if input_text[x][0] in num_list:
            num_list.remove(input_text[x][0])
        x += 1
    while y < len(input_text):
        if input_text[y][1] in num_list:
            num_list.remove(input_text[y][1])
        y += 1
    return sorted(num_list)

print("These numbers could be telemarketers: ")
print('\n'.join(output_list(texts,calls)))

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字母顺序输出。
"""
