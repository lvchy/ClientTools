# -*- coding: utf-8 -*-

import os.path
from operator import attrgetter

import common
import utfile
import utrequest
import localinfo

_downloadOnline = False
_hasChange = False
_totalChangeSize = 0

def _deployConfig():
    buildRoot = common.getBuildRoot()
    deployRoot = common.getDeployRoot()

    # verpath = os.path.join(buildRoot, common.CONFIG_VER_NAME)
    # if _downloadOnline:
    #     md5local = utfile.loadFile(verpath).split('|')[1]
    #     remote = utrequest.downloadText(common.getUabUrl(common.CONFIG_VER_NAME))
    #     print('remote', common.getUabUrl(common.CONFIG_VER_NAME), remote)
    #     md5remote = remote.split('|')[1]
    #     if md5local == md5remote:
    #         return
    print('------------ deploy cfg')
    utfile.copy(os.path.join(buildRoot, common.CONFIG_NAME), os.path.join(deployRoot, common.CONFIG_NAME))
    # utfile.copy(os.path.join(buildRoot, common.CONFIG_VER_NAME), os.path.join(deployRoot, common.CONFIG_VER_NAME))

def _deployUab():
    buildRoot = common.getBuildRoot()
    deployRoot = common.getDeployRoot()

    global _hasChange
    _hasChange = False

    jdlocal = utfile.loadJsonFile(os.path.join(buildRoot, common.INFO_NAME))
    jdremote = {'G': []}
    if _downloadOnline:
        jdremote = utrequest.downloadJson(common.getUabUrl(common.INFO_NAME))
    maplocal = common.transInfo(jdlocal)
    mapremote = common.transInfo(jdremote)
    diffuabs = []
    for k, v in maplocal.items():
        if (k not in mapremote) or (v['H'] != mapremote[k]['H']):
            _hasChange = True
            diffuabs.append(os.path.join(buildRoot, common.UAB_BUNDLE_ROOT, k))
            print('------------ deploy uab', k, common.svnversion)
        else:
            v['V'] = mapremote[k]['V']
    if _hasChange:
        _copyUab(diffuabs)
        jdnew = {'G': []}
        for _, v in maplocal.items():
            jdnew['G'].append(v)
        utfile.writeJsonToFile(os.path.join(deployRoot, common.INFO_NAME), jdnew)
        # utfile.writeToFile(os.path.join(deployRoot, common.INFO_VER_NAME), common.svnversion)

def _deployV():
    deployRoot = common.getDeployRoot()
    vpath = os.path.join(deployRoot, common.VER_NAME)
    utfile.writeToFile(vpath, common.svnversion)

def _copyUab(diffuabs):
    buildRoot = common.getBuildRoot()
    deployRoot = common.getDeployRoot()

    global _totalChangeSize
    for uab in diffuabs:
        utfile.copy(uab, uab.replace(buildRoot, deployRoot))
        _totalChangeSize = _totalChangeSize + utfile.getsize(uab)

def copy2nas(deployRoot):
    nasuabroot = common.getNasUabRoot()
    utfile.ensureDir(nasuabroot)
    nasbundleroot = os.path.join(nasuabroot, common.UAB_BUNDLE_ROOT)
    utfile.ensureDir(nasbundleroot)

    utfile.copyfolder(deployRoot, nasuabroot)


def deploy(downloadOnline=False, onlyBinary=False):
    global _downloadOnline
    # _downloadOnline = downloadOnline
    _downloadOnline = False

    deployRoot = common.getDeployRoot()
    utfile.ensureDir(deployRoot, True)

    localinfo.create(onlyBinary)
    _deployConfig()
    _deployUab()
    _deployV()

    copy2nas(deployRoot)
    print('done deploy...')


if __name__ == "__main__":
    # deploy(r'C:\work\repository\Raid\Client\1.0', 'Android', True)
    # deploy('C:/work/repository/projectrain_clean/Tools/BuildTextUab/work', 'Editor')
    # deploy(r'c:\work\jenkins\svn\1.0', 'Android', True, False)
    pass
