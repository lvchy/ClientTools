# -*- coding: utf-8 -*-

import zipfile
import json
import hashlib
import os
import shutil

def writeToFile(path, content):
    f = open(path, 'w', encoding='utf-8')
    f.write(content)
    f.close()

def writeJsonToFile(path, jd, indent=4):
    data = json.dumps(jd, indent=indent)
    writeToFile(path, data)

def loadFile(path):
    if not os.path.exists(path):
        return None
    f = open(path, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    return content

def loadJsonFile(path):
    if not os.path.exists(path):
        return None
    content = loadFile(path)
    return json.loads(content)

def calcTextMd5(text):
    md5 = hashlib.md5(text.encode('utf8')).hexdigest()
    return str(md5).lower()

def calcFileMd5(path):
    f = open(path, 'rb')
    md5 = hashlib.md5()
    while True:
        d = f.read(8096)
        if not d:
            break
        md5.update(d)
    hashcode = md5.hexdigest()
    f.close()
    return str(hashcode).lower()

def skipFile(file, extension=None):
    return file.endswith('.meta') or file.startswith('.') or (extension != None and not file.endswith(extension))

def zipfolder(dir, target, extension=None):
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(dir):
            for file in files:
                if skipFile(file, extension):
                    continue
                filepath = os.path.join(root, file)
                arcname = filepath[len(dir)+1:]
                z.write(filepath, arcname=arcname)

def copyfolder(srcroot, tarroot, extension=None, newextension=None, cbpre=None, cbpost=None):
    for root, _, files in os.walk(srcroot):
        for file in files:
            if skipFile(file, extension):
                continue
            srcfilepath = os.path.join(root, file)
            tarfilepath = os.path.join(tarroot, srcfilepath[len(srcroot)+1:])
            if cbpre is not None:
                tarfilepath = cbpre(tarfilepath)
            if newextension != None:
                tarfilepath = changeext(tarfilepath, newextension)
                # tarfilepath = os.path.splitext(tarfilepath)[0]+newextension
            copy(srcfilepath, tarfilepath)
            if cbpost is not None:
                cbpost(tarfilepath)

def copy(src, dst):
    if not os.path.exists(src):
        return
    dirname = os.path.dirname(dst)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    shutil.copyfile(src, dst)

def ensureDir(dir, recreate=False):
    if os.path.exists(dir) and recreate:
        shutil.rmtree(dir)
    if not os.path.exists(dir):
        os.mkdir(dir)

def rmfile(file):
    os.remove(file)

def changeext(file, ext):
    return os.path.splitext(file)[0] + ext

def getsize(file):
    return os.path.getsize(file)