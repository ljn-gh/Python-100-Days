"""
从文本文件中读取数据
"""


def readFileAll():
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def readList():
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(lines)


def readLine():
    try:
        with open('致橡树.txt', 'r',encoding='utf-8') as f:
            for line in f:
                print(line, end='')
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        f.close()

if __name__ == '__main__':
    while True:
        mode = input('读取方式(all, line, list, e): ')
