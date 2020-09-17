import sys
import getopt
import common

outs = []

ARG_CMD = 'cmd'
ARG_WORKROOT = 'workroot'
ARG_PLATFORM = 'platform'
ARG_SVNVER = 'svnver'
ARG_PKGUSAGE = 'pkgusage'
ARG_DOWNLOAD = 'download'
ARG_ONLYBUILTIN = 'onlybuiltin'
ARG_ONLYBINARY = 'onlybinary'
ARG_SEND_DINGDING = 'senddd'
ARG_PKG_DESC = 'pkgdesc'
ARG_UAB_DESC = 'uabdesc'

CMD_BUILD_BINARY = 'cmd_buildbinary'
CMD_DEPLOY = 'cmd_deploy'
CMD_COPY2STREAM = 'cmd_copy2stream'
CMD_POSTBUILD_PKG = 'cmd_postbuild_pkg'
CMD_POSTBUILD_UAB = 'cmd_postbuild_uab'

args = {}
def _arg(s):
    return s[2:]
def _opt(l):
    rtn = []
    for v in l:
        rtn.append(v+'=')
    return rtn
def _parseArgs():
    l = [
        ARG_CMD,
        ARG_WORKROOT,
        ARG_PLATFORM,
        ARG_SVNVER,
        ARG_PKGUSAGE,
        ARG_DOWNLOAD,
        ARG_ONLYBUILTIN,
        ARG_ONLYBINARY,
        ARG_SEND_DINGDING,
        ARG_PKG_DESC,
        ARG_UAB_DESC,
    ]
    opts, _ = getopt.getopt(sys.argv[1:], '', _opt(l))
    d = {}
    for opt, arg in opts:
        d[_arg(opt)] = arg
    for v in l:
        if v in d:
            args[v] = d[v]
        else:
            args[v] = None
    print(args)

def run():
    _parseArgs()

    cmd = args[ARG_CMD]
    workroot = args[ARG_WORKROOT]
    platform = args[ARG_PLATFORM]
    svnver = args[ARG_SVNVER]
    if svnver == None:
        import utsvn
        svnver = utsvn.getVersion(workroot)
    pkgusage = args[ARG_PKGUSAGE]

    download = False
    if args[ARG_DOWNLOAD] != None:
        download = args[ARG_DOWNLOAD].lower() == 'true'
    
    onlybuiltin = False
    if args[ARG_ONLYBUILTIN] != None:
        onlybuiltin = args[ARG_ONLYBUILTIN].lower() == 'true'

    onlybinary = False
    if args[ARG_ONLYBINARY] != None:
        onlybinary = args[ARG_ONLYBINARY].lower() == 'true'
    
    sendDingding = False
    if args[ARG_SEND_DINGDING] != None:
        sendDingding = args[ARG_SEND_DINGDING].lower() == 'true'
    
    pkgdesc = None
    if args[ARG_PKG_DESC] != None:
        pkgdesc = args[ARG_PKG_DESC]
    
    uabdesc = None
    if args[ARG_UAB_DESC] != None:
        uabdesc = args[ARG_UAB_DESC]
    
    print(cmd, workroot, pkgusage, platform, svnver, download, onlybuiltin, onlybinary)

    common.workroot = workroot
    common.platform = platform
    common.svnversion = svnver
    common.pkgusage = pkgusage

    if cmd == CMD_BUILD_BINARY:
        import binarybuild
        binarybuild.build()
    elif cmd == CMD_DEPLOY:
        import deploy
        deploy.deploy(download, onlybinary)
    elif cmd == CMD_COPY2STREAM:
        import copy2streaming
        copy2streaming.copy(onlybuiltin)
    elif cmd == CMD_POSTBUILD_PKG:
        import post_build_pkg
        post_build_pkg.build(sendDingding, pkgdesc)
    elif cmd == CMD_POSTBUILD_UAB:
        import post_build_uab
        post_build_uab.build(sendDingding, uabdesc)

if __name__ == "__main__":
    print('start python runner...')
    print(sys.argv)
    run()
    print('done python runner...')