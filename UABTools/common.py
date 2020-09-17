# -*- coding: utf-8 -*-

import os.path
import os
import utfile

IS_BINARY_KEY = 'isbinary'
BUILTIN_KEY = 'builtin'
ASSET_PATH_KEY = 'assetpath'
EXTENSION_KEY = 'extensions'
UAB_COUNT_KEY = 'uabcount'

UAB_NAME_KEY = 'name'
UAB_EXT = '.u'

WORKROOT_ASSETS_PATH = 'Assets'
WORKROOT_CONFIG_PATH = 'Assets/Standard Assets/UAB/cfg.txt'
WORKROOT_STREAMINGASSETS_PATH = 'Assets/StreamingAssets/uab'
WORKROOT_BUILTIN_CFG_PATH = 'Assets/Resources/Builtin/builtin_cfg.txt'

DEPLOYROOT = 'deploy/{}'
BUILDROOT = 'uab/{}'

UAB_BUNDLE_ROOT = 'bundles'

INFO_NAME = 'info'
CONFIG_NAME = 'cfg'
VER_NAME = 'v'

BINARY_INFO_NAME = 'binaryinfo'
ASSET_INFO_NAME = 'assetinfo'

KEY_RESOURCESROOT = '{ResourcesRoot}'
RESOURCESROOT = 'ResourcesAB'

workroot = None
platform = None
svnversion = None
pkgusage = None

NAS_URL_BASE = 'http://raid-gs.diandian.info:7200/client'
NAS_URL_UAB = NAS_URL_BASE + '/uab/{}/{}'
NAS_URL_PKG = NAS_URL_BASE + '/package/{}/{}'

NAS_FOLDER_BASE = r'\\nas.centurygamesh.io\Public\deployment\release'
NAS_FOLDER_UAB = NAS_FOLDER_BASE + '\\uab\\'
NAS_FOLDER_PKG = NAS_FOLDER_BASE + r'\package\{}\{}'

DINGDING_POST_TEXT = 'http://10.1.70.66:10000/client/send_text'
DINGDING_POST_LINK = 'http://10.1.70.66:10000/client/send_link'
DINGDING_PIC_URL = 'https://i.ibb.co/30Sqfmc/image.png'


def getBuildRoot():
    root = os.path.join(workroot, BUILDROOT.split('/')[0])
    utfile.ensureDir(root)
    return os.path.abspath(os.path.join(workroot, BUILDROOT).format(platform))

def getDeployRoot():
    root = os.path.join(workroot, DEPLOYROOT.split('/')[0])
    utfile.ensureDir(root)
    return os.path.abspath(os.path.join(workroot, DEPLOYROOT).format(platform))

def getStreamingRoot():
    return os.path.abspath(os.path.join(workroot, WORKROOT_STREAMINGASSETS_PATH))

def getUabUrl(path):
    return NAS_URL_UAB.format(pkgusage, platform)+'/'+path

def getNasUabRoot():
    jd = utfile.loadJsonFile(os.path.join(workroot, WORKROOT_BUILTIN_CFG_PATH))
    root = NAS_FOLDER_UAB + '{}.{}'.format(jd['version'], svnversion)
    utfile.ensureDir(root)
    root = root + '\\{}'.format(platform)
    utfile.ensureDir(root)
    return root
    # if pkgusage.lower() == 'raid-test':
    #     return NAS_FOLDER_UAB + 'raid-test\\' + platform
    # else:
    #     jd = utfile.loadJsonFile(os.path.join(workroot, WORKROOT_BUILTIN_CFG_PATH))
    #     return NAS_FOLDER_UAB + '{}.{}'.format(jd['version'], svnversion)

def transInfo(jd):
    info = {}
    for item in jd['G']:
        info[item['N']] = item
    return info

def getUabGroup(uabfile):
    if '_' in uabfile:
        idx = uabfile.index('_')
        return uabfile[:idx]
    else:
        return os.path.splitext(uabfile)[0]