import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

BanCall = []
result = []
BanCallBan = []
for num in calls:
    if num[0][:5] == '(080)':
        BanCall.append(num[1])
for eve in BanCall:
    if eve[0] == '(':
        index = eve.find(')')
        result.append(eve[1:index])
        if eve[:5] == '(080)':
            BanCallBan.append(eve)
    if ' ' in eve:
        result.append(eve[:4])
print("The numbers called by people in Bangalore have codes:")
print("\n".join(sorted(set(result))))
print("{:.2%} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format((len(BanCallBan) / len(BanCall))))
