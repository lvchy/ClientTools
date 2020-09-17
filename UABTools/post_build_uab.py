import os
import os.path

import common
import utfile

import utrequest

def build(sendDingding=False, uabdesc=None):
  if not sendDingding:
    return
  
  ddtext = '客户端资源已部署好! '
  if uabdesc != None and uabdesc != '':
    ddtext = ddtext + '[ {} ]'.format(uabdesc)
  ddtext = ddtext + '[ {} ]'.format(common.svnversion)
  print('ddtext', ddtext)
  utrequest.postDingdingText(ddtext)

if __name__ == "__main__":
  common.workroot = 'c:/work/jenkins/svn/1.0'
  common.platform = 'Android'
  build(True)
  pass