#!/usr/bin/env python

import ftplib
import os
import fnmatch
import socket
import logging

logger = logging.getLogger('setupEnv.downloadBuild')


class FTPSync(object):
    conn = ftplib.FTP()  # static variable

    def __init__(self, host, port=21):
        self.conn.connect(host, port)

    def login(self, username, password):
        self.conn.login(username, password)
        self.conn.set_pasv(False)
        # logger.info(self.conn.welcome)
        print(self.conn.welcome)

    def listDir(self, ftppath):
        dir_res = []
        self.conn.dir(ftppath, dir_res.append)
        dirs = [k.split(None, 8)[-1] for k in dir_res if k.startswith('d')]
        # print(dirs)
        return dirs

    def listFile(self, ftppath):
        file_res = []
        self.conn.dir(ftppath, file_res.append)
        files = [k.split(None, 8)[-1] for k in file_res if k.startswith('-')]
        # print(file_res)
        return files

    def isDir(self, ftppath, filename):
        pass

    def cwdDir(self, ftppath):
        try:
            self.conn.cwd(ftppath)
        except ftplib.error_perm:
            logger.error('ERROR: cannot CD to "%s"' % ftppath)
            self.conn.quit()
            return
        logger.info('*** Changed to "%s" folder' % ftppath)

    def downloadFile(self, ftppath, filename):
        try:
            self.conn.cwd(ftppath)
            ftp_curr_path = self.conn.pwd()
            print('*** ftp current path  - "%s"' % ftp_curr_path)
            self.conn.retrbinary('RETR %s' % filename, open(filename, 'wb').write)
            # os.chdir(workdir)
        except ftplib.error_perm:
            print('ERROR: cannot read file "%s"' % filename)
            os.unlink(filename)
        else:
            print('*** downloaded "%s" to local directory' % filename)

    def uploadFile(self, filename):
        try:
            ftp_curr_path = self.conn.pwd()
            print('*** ftp current path  - "%s"' % ftp_curr_path)
            self.conn.storbinary('STOR %s' % filename, open(filename, 'rb'))
        except ftplib.error_perm:
            print('ERROR: cannot read file "%s"' % filename)
            os.unlink(filename)
        else:
            print('*** uploaded "%s" to ftp' % filename)

    def downloadFileTree(self, nextdir):
        try:
            self.conn.cwd(nextdir)
            if not os.path.exists(nextdir):
                os.mkdir(nextdir)
            os.chdir(nextdir)

            ftp_curr_path = self.conn.pwd()
            local_curr_path = os.getcwd()
            # 1. files - directly download
            files = self.listFile(ftp_curr_path)
            for f in files:
                print('****File: ', f)
                print('****File: ftp curr path:', ftp_curr_path)
                print('****File: local curr path:', local_curr_path)
                self.conn.retrbinary('RETR %s' % f, open(f, 'wb').write)
                print('*** Downloaded "%s" to "%s"' % (f, ftp_curr_path))
            # 2. directorires - recursively download files
            dirs = self.listDir(ftp_curr_path)
            for d in dirs:
                print('Folder - ', d)
                print('****Folder: ftp curr path:', ftp_curr_path)
                print('****Folder: local curr path:', local_curr_path)
                os.chdir(local_curr_path)
                self.conn.cwd(ftp_curr_path)
                self.downloadFileTree(d)
        except ftplib.error_perm:
            print('ERROR: cannot read file "%s"' % f)
            os.unlink(f)

    def downloadWildcard(self, ftppath, wildcard):
        files = self.listFile(ftppath)
        for f in files:
            if fnmatch.fnmatch(f, wildcard):
                print(f)
                self.downloadFile(f)



    def quit(self):
        self.conn.quit()


if __name__ == '__main__':
    dirname = 'download'
    host = '83.28.225.94'
    workdir = os.getcwd()
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    os.chdir(dirname)

    # ftp = FTPSync(host)
    # ftp.login('wasup', 'wasup123')
    # ftp.cwdDir('/home/wasup/testftp')
    # # ftp.downloadFile('forDownload.txt')
    # # ftp.uploadFile('forUpload.txt')
    # ftp.downloadFileTree('.')
    # ftp.quit()
    # os.chdir(workdir)
    #
    # # with open('test.txt', 'rb') as f:
    # #     lines = f.readlines()
    # #     for line in lines:
    # #         print(line)
    # print(os.getcwd())

    files = os.listdir('/Users/liuqq/PycharmProjects/qqsite/util')
    print(files)
    for f in files:
        if fnmatch.fnmatch(f, '*.py'):
            # self.downloadFile(f)
            print(f)




