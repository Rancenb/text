import csv

# 读取测试数据并转换为一个列表
with open('fyx_chinamoney.csv', 'r') as f:
    reader = csv.reader(f)
    data = [row for row in reader]

# 将列表切分成长度为80的子列表
batch_size = 80
batches = [data[i:i+batch_size] for i in range(0, len(data), batch_size)]

# 打印输出每个子列表
for batch in batches:
    print(batch)