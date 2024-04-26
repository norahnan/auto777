# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':

    #files =
    import json

    # 假设有三个JSON文件：file1.json、file2.json和file3.json
    files = ['data/016209.json']
    import os

    # 指定路径
    path = 'data/'

    # 获取所有文件名
    filenames = os.listdir(path)

    # 过滤出需要的文件类型，例如txt文件
    files = [f for f in filenames if f.endswith('.json')]


    data = []

    for file in files:
        with open('data/'+file, 'r', encoding='utf-8') as f:
            data.append(json.load(f))

    print(data[:3])

    print(len(data))

    import csv

    # 定义字典




    print('第一条数据：',data[0])

    newData = []
    for item in data:
        temp = []
        temp.append(item['cause']+'。'+item['question'])
        temp.append(''.join(item['candidate_answer']))
        newData.append(temp)

    # Specify the file name
    filename = 'law.csv'

    # Write the list to a CSV file
    with open(filename, 'w', newline='',encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(newData)

    print(f'{filename} created successfully.')



