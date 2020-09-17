import utfile
import common
import os.path
import os
import localinfo

_builtinGrps = {}

def _copyCfg():
    buildRoot = common.getBuildRoot()
    streamingRoot = common.getStreamingRoot()

    utfile.copy(os.path.join(buildRoot, common.CONFIG_NAME), os.path.join(streamingRoot, common.CONFIG_NAME))
    # utfile.copy(os.path.join(buildRoot, common.CONFIG_VER_NAME), os.path.join(streamingRoot, common.CONFIG_VER_NAME))

def _copyUab():
    buildRoot = common.getBuildRoot()
    streamingRoot = common.getStreamingRoot()

    utfile.copy(os.path.join(buildRoot, common.INFO_NAME), os.path.join(streamingRoot, common.INFO_NAME))
    # utfile.copy(os.path.join(buildRoot, common.INFO_VER_NAME), os.path.join(streamingRoot, common.INFO_VER_NAME))

    jdinfo = utfile.loadJsonFile(os.path.join(streamingRoot, common.INFO_NAME))
    for v in jdinfo['G']:
        file = v['N']
        utfile.copy(os.path.join(buildRoot, common.UAB_BUNDLE_ROOT, file), os.path.join(streamingRoot, common.UAB_BUNDLE_ROOT, file))

def _copyV():
    streamingRoot = common.getStreamingRoot()
    vpath = os.path.join(streamingRoot, common.VER_NAME)
    utfile.writeToFile(vpath, common.svnversion)

def copy(onlyBuiltin=False):
    utfile.ensureDir(common.getStreamingRoot(), True)

    localinfo.create(False, onlyBuiltin)

    _copyCfg()
    _copyUab()
    _copyV()

    print('done...')

if __name__ == "__main__":
    # copy('C:/work/repository/projectrain_clean/ProjectRain', 'Android', True)
    # common.workroot = 'E:/git/projectrain/ProjectRain'
    # _copyvideo()
    pass