import csv
import os
import json

#读取txt 以,,分段
def readTxt(fileN):
    data = []
    with open(fileN,"r", encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip("\n")
            line = line.split(',,')
            data.append(line)
    #print(data)
    return data


if __name__ == '__main__':


    #只取最后为1的数据
    datains = readTxt('ins.txt')
    print(len(datains))
    datanew = []
    for item in datains:
        if item[-1][-1] == '1':
            datanew.append(item)

    abn = 0



    #3788
    #找到长度不是2 的 以您好分割，不行就用逗号分，分完去掉最后的1
    for item in datanew:
        if len(item) > 2:
            datanew.remove(item)

        elif len(item) != 2:
            abn += 1
            #print(len(item))
            temp = item[0].split('您好')

            if len(temp) == 1:
                temp = temp[0].split(',')
                if '1' in temp:
                    temp.remove('1')
                if len(temp) == 3:
                    temp = temp[1:]

            datanew.remove(item)
            datanew.append(temp)
            #print(len(temp),temp)

    print(abn)

    #还有问题的就删 但是删+循环容易出问题，建议新建列表
    tp = 0
    for item in datanew:
        if len(item) != 2:
            tp += 1
            #print(len(item),item)
            datanew.remove(item)
    print(len(datanew))

    for item in datanew:

        if len(item) != 2:
            print(len(item), item)
            datanew.remove(item)

    for item in datanew:
        if len(item) != 2:
            #print(item)
            datanew.remove(item)

    for item in datanew:
        if len(item) != 2:
            print(item)

    #找到问题相同的删了
    qs = {}
    for item in datanew:
        if item[0] not in qs.keys():
            #print(len(item))
            qs[item[0]] = item[1]

        else:
            del qs[item[0]]
            print(item)
    print(len(datanew))






    # # Specify the file name
    # filename = 'ins.csv'
    #
    # # Write the list to a CSV file
    # with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    #     csvwriter = csv.writer(csvfile)
    #     csvwriter.writerows(datanew)
    #
    # print(f'{filename} created successfully.')
