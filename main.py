import os
import csv
import time

type_list = ['.md', '.csv', '.pdf', '.txt', '.png', '.html', '.xml', '.py', '其他', '文件夹']
type_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def create_csv(pathname, index):
    path = "resList.csv"
    with open(path, 'w+', newline='') as f:
        csv_write = csv.writer(f)
        get_list(pathname, index, csv_write)


def get_list(pathname, index, csv_write):
    for files in os.listdir(pathname):
        ind = 8
        type_count[ind] = type_count[ind] + 1
        current_file = pathname + '\\' + files
        list1 = []
        for i in range(index):
            list1.append('|--------')
        list1.append(files)
        print(list1)
        csv_write.writerow(list1)
        #  print('|---' * index + files)
        if os.path.isdir(current_file):
            type_count[9] = type_count[9] + 1
            get_list(current_file, index + 1, csv_write)
        try:
            ind = type_list.index(os.path.splitext(files)[1])
            type_count[ind] = type_count[ind] + 1
        except:
            type_count[ind] = type_count[ind] + 1
            continue


if __name__ == '__main__':
    current_dir = os.getcwd()
    path = r'D:\markdown'
    create_csv(current_dir, 1)
    for i in range(len(type_list)):
        print(type_list[int(i)] + ':' + str(type_count[int(i)]))
    time.sleep(10)