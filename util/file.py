import os
import sys
import shutil
import platform


# recursivelly delete directory
def delRurDir(filepath):
    shutil.rmtree(filepath)


# delete one file
def delFile(filepath):
    os.remove(filepath)


def readFile(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            print(line)


def writeFile(filepath):
    with open(filepath, 'a') as f:
        f.write("Add one line to file\n")


def zipFolder(folder):
    shutil.make_archive('archive', 'zip', folder)


def unzipFolder(zipfile):
    shutil.unpack_archive(zipfile, 'outside')


def replaceOnefile(filename, valDict):
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()

        for line in lines:
            for key in valDict:
                line = line.replace(key, valDict.get(key))
            f.write(line)


def replaceConfigParm(filename, valdict):
    with open(filename, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()

        for line in lines:
            if line.find('=') != -1:
                parm = line.split("=")[0].strip()
                var = line.split("=")[1].strip()
                for key, value in valdict.items():
                    if parm == key:
                        if var == '':
                            line = line.strip() + value + '\n'
                            print(line)
                        else:
                            line = line.replace(var, value)
            f.write(line)


if __name__ == '__main__':
    # readFile('test/test.log')
    # writeFile('test/test.log')
    # zipFolder('test')
    # unzipFolder('archive.zip')
    # valdict = {'@ip@': '9.181.128.214', '@host@': 'www.baidu.com'}
    # replaceOnefile('../test/test.conf', valdict)

    # valdict = {'Maker.Port': '9999', 'EngineType': 'Simple', 'testSpace': 'HopeOK'}
    # # valdict = {'host': '1111', 'address':'street'}
    # replaceConfigParm('../test/Settings.properties', valdict)

    # print(sys.stdin.encoding)

    # str1 = 'host=@host@'
    # str2 = 'ip=@ip@'
    # str3 = 'address= '

    # a1 = str3.split("=")[0].strip()
    # print(a1)
    # b1 = str3.split("=")[1].strip()
    # print(b1)
    delFile('../test/ttt/aaa')








