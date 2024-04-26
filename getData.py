# with open('testM.txt', 'r', encoding='utf-8') as f:
#     data = f.readline()
#     print(data)


def readTxt(fileN):
    data = []
    with open(fileN,"r", encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip("\n")
            line = line.split()
            data.append(line)
    #print(data)
    return data


if __name__ == '__main__':

        rt = readTxt('testM.txt')

        #print(len(rt))


        canrt = []
        for item in rt:
            if '癌' in item[1] or '癌' in item[2]:
                canrt.append(item)

        # print(len(canrt), canrt[75])

        print(rt[7])

        # for item in rt:
        #     if len(item[1])<7:
        #         print(item)

        import csv

        # # Example list
        # data = rt[:2300]
        #
        # # Specify the file name
        # filename = 'med2000.csv'
        #
        # # Write the list to a CSV file
        # with open(filename, 'w', newline='',encoding='utf-8') as csvfile:
        #     csvwriter = csv.writer(csvfile)
        #     csvwriter.writerows(data)
        #
        # print(f'{filename} created successfully.')

        import json

        # Specify the path to the JSON file
        json_file_path = '*.json'
        whole = []

        from pathlib import Path

        files = Path('').glob('*.json')  # get all csvs in your dir.
        for file in files:

            # Open the JSON file and load the data
            with open(file, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                whole.append(data)

        # Now, 'data' contains the parsed JSON data
        #print(whole)
        #print(type(data))




