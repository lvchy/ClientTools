import svn.local

import common

def getVersion(root=None):
  if root == None:
    root = common.workroot
  r = svn.local.LocalClient(root)
  info = r.info()
  return str(info['entry_revision'])

if __name__ == "__main__":
    # getVersion(r'c:\work\repository\Raid-new\Client\1.0')
    getVersion(r'c:\work\jenkins\svn\1.0')