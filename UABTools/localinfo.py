# -*- coding: utf-8 -*-

import os.path
from operator import attrgetter

import common
import utfile
import utftp
import utrequest

def _config():
    buildRoot = common.getBuildRoot()
    cfgpath = os.path.join(buildRoot, common.CONFIG_NAME)
    jdcfg = utfile.loadJsonFile(cfgpath)
    jdcfg['G'] = sorted(jdcfg['G'], key=lambda x: x['name'])
    utfile.writeJsonToFile(cfgpath, jdcfg)

def _collectUabs(infopath, usegrps, info):
    jd = utfile.loadJsonFile(infopath)
    for v in jd['G']:
        grp = common.getUabGroup(v['N'])
        if grp in usegrps:
            info['G'].append(v)

def _uab(onlyBinary, onlyBuiltin):
    buildRoot = common.getBuildRoot()
    cfgpath = os.path.join(buildRoot, common.CONFIG_NAME)
    jdcfg = utfile.loadJsonFile(cfgpath)
    usegrps = {}
    for v in jdcfg['G']:
        if (not onlyBinary or (common.IS_BINARY_KEY in v and v[common.IS_BINARY_KEY])) and (not onlyBuiltin or (common.BUILTIN_KEY in v and v[common.BUILTIN_KEY])):
            usegrps[v['name']] = True

    info = {'G':[]}
    assetpath = os.path.join(buildRoot, common.ASSET_INFO_NAME)
    if not onlyBinary:
        _collectUabs(assetpath, usegrps, info)
    binarypath = os.path.join(buildRoot, common.BINARY_INFO_NAME)
    _collectUabs(binarypath, usegrps, info)

    for v in info['G']:
        v['V'] = common.svnversion
        if 'R' in v:
            del(v['R'])
    
    utfile.writeJsonToFile(os.path.join(buildRoot, common.INFO_NAME), info)

def _ver():
    buildRoot = common.getBuildRoot()
    verpath = os.path.join(buildRoot, common.VER_NAME)
    utfile.writeToFile(verpath, common.svnversion)

def create(onlyBinary=False, onlyBuiltin=False):
    _config()
    _uab(onlyBinary, onlyBuiltin)
    _ver()