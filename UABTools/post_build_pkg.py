import os
import os.path

import common
import utfile

import utrequest

def build(sendDingding=False, pkgdesc=None):
  if not sendDingding:
    return
  
  pkgtmp = os.path.join(common.workroot, '_package/pkgtmp.txt')
  f = open(pkgtmp, 'r', encoding='utf-8')
  lines = f.readlines()
  f.close()
  pkgpath = lines[0].strip()
  pkgurl = pkgpath.replace(common.NAS_FOLDER_BASE, common.NAS_URL_BASE).replace('\\', '/')
  obbpath = None
  obburl = None
  if len(lines) == 2:
    obbpath = lines[1].strip()
    obburl = obbpath.replace(common.NAS_FOLDER_BASE, common.NAS_URL_BASE).replace('\\', '/')

  ddtext = '包类型 [ {} ]. 版本号 [ {} ].'.format(common.pkgusage, common.svnversion)
  if pkgdesc != None and pkgdesc != '':
    ddtext = ddtext + '\n' + pkgdesc
  utrequest.postDingdingLink({
    'title': '包已出好! [ {} ]'.format(common.platform),
    'text': ddtext,
    'messageUrl': pkgurl,
    'picUrl': common.DINGDING_PIC_URL,
  })

  if obburl != None and obburl != '':
    utrequest.postDingdingLink({
      'title': '包已出好! [ obb ]',
      'text': ddtext,
      'messageUrl': obburl,
      'picUrl': common.DINGDING_PIC_URL,
    })

if __name__ == "__main__":
  common.workroot = 'c:/work/jenkins/svn/1.0'
  common.platform = 'Android'
  build(True)
  pass