# -*- coding: utf-8 -*-

import ftplib
import os
import os.path

import common

HOST = '212.129.152.27'
PORT = 21
USER = 'ubuntu'
PASSWORD = 'ZTElzh0203'

def _connect():
    ftp = ftplib.FTP()
    ftp.connect(HOST, PORT)
    ftp.login(USER, PASSWORD)
    return ftp

def _uploadOne(ftp, remote, local):
    bufsize = 1024
    fp = open(local, 'rb')
    ftp.storbinary('STOR '+remote, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()
    print('upload one: ', remote)

def _uploadFolderTop(ftp, dir, root):
    if not os.path.exists(dir):
        return
    basename = os.path.basename(root)
    files = os.listdir(dir)
    for file in files:
        fpath = os.path.join(dir, file).replace('\\', '/')
        if not os.path.isfile(fpath):
            continue
        relativepath = basename+'/'+fpath[len(root)+1:]
        _uploadOne(ftp, relativepath, fpath)

# 先上传uab，最后上传配置文件
def upload(root):
    ftp = _connect()

    bundleRoot = os.path.join(root, common.UAB_BUNDLE_ROOT)
    _uploadFolderTop(ftp, bundleRoot, root)

    _uploadFolderTop(ftp, root, root)

    ftp.close()

    print('done upload...')

if __name__ == '__main__':
    # upload('C:/work/repository/projectrain_clean/ProjectRain/deploy/Android')
    upload('C:/work/repository/projectrain_clean/Tools/BuildTextUab/work')