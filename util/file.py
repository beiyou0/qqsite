import sys
import shutil

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
    f = open(filename, 'r+')
    lines = f.readlines()
    f.seek(0)
    f.truncate()

    for line in lines:
        for key in valDict:
            line = line.replace(key, valDict.get(key))
        f.write(line)
    f.close()


def replaceConfigParm(filepath, valdict):
    with open(filepath, 'r+', encoding='utf-8') as f:
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
                        else:
                            line = line.replace(var, value)
            print(line)
            f.write(line)




if __name__ == '__main__':
    # readFile('test/test.log')
    # writeFile('test/test.log')
    # zipFolder('test')
    # unzipFolder('archive.zip')
    # valdict = {'@ip@': '9.181.128.214', '@host@': 'www.baidu.com'}
    # replaceOnefile('test/test.conf', valdict)

    # print(sys.stdin.encoding)
    # print(sys.stdout.encoding)
    valdict = {'ip': '9.181.128.214', 'addr':'street no.', 'email':'111@163.com'}
    replaceConfigParm('util/test/test.conf', valdict)