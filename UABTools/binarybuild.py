# -*- coding: utf-8 -*-

import json
import os.path
import common
import utfile
import encrypt
import localinfo

_binaryinfo = None
_currgrp = None

def _buildFromConfig():
    global _binaryinfo
    global _currgrp
    jd = utfile.loadJsonFile(os.path.join(common.workroot, common.WORKROOT_CONFIG_PATH))
    for _, v in enumerate(jd['G']):
        if not common.IS_BINARY_KEY in v or not v[common.IS_BINARY_KEY]:
            continue
        _currgrp = v
        assetroot = os.path.join(common.workroot, common.WORKROOT_ASSETS_PATH, v[common.ASSET_PATH_KEY]).replace(common.KEY_RESOURCESROOT, common.RESOURCESROOT)
        uabcount = v[common.UAB_COUNT_KEY]
        if uabcount < 0:
            tarroot = os.path.join(common.getBuildRoot(), common.UAB_BUNDLE_ROOT)
            utfile.copyfolder(assetroot, tarroot, v[common.EXTENSION_KEY], common.UAB_EXT, preprocess, postprocess)
        else:
            target = os.path.join(common.getBuildRoot(), common.UAB_BUNDLE_ROOT, _currgrp[common.UAB_NAME_KEY]+common.UAB_EXT)
            utfile.zipfolder(assetroot, target, v[common.EXTENSION_KEY])
            postprocess(target)

def preprocess(file):
    basename = os.path.basename(file)
    return file.replace(basename, _currgrp[common.UAB_NAME_KEY]+'_'+basename).lower()
    
def postprocess(file):
    if not ('noencrypt' in _currgrp) or not _currgrp['noencrypt']:
        encrypt.encryptFile(file)
    global _binaryinfo
    _binaryinfo['G'].append({
        'N':os.path.basename(file).lower(),
        'S':os.path.getsize(file),
        'H':utfile.calcFileMd5(file),
    })

def _createConfig():
    cfgpath = os.path.join(common.workroot, common.WORKROOT_CONFIG_PATH)
    tarpath = os.path.join(common.getBuildRoot(), common.CONFIG_NAME)
    utfile.copy(cfgpath, tarpath)

def _createInfo():
    infopath = os.path.join(common.getBuildRoot(), common.BINARY_INFO_NAME)
    utfile.writeJsonToFile(infopath, _binaryinfo)

def build():
    global _binaryinfo

    buildRoot = common.getBuildRoot()
    utfile.ensureDir(buildRoot)
    utfile.ensureDir(os.path.join(buildRoot, common.UAB_BUNDLE_ROOT), False)

    _binaryinfo = {'G':[]}
    _buildFromConfig()
    
    _createConfig()
    _createInfo()
    
    print('done build binary ...')


if __name__ == "__main__":
    # build(r'D:\svn\Raid\Client\1.0', 'Android')
    pass