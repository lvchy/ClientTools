import sys
import utfile
import common

def compare():
  afile = sys.argv[1]
  bfile = sys.argv[2]

  adata = utfile.loadJsonFile(afile)
  bdata = utfile.loadJsonFile(bfile)

  adict = common.transInfo(adata)
  bdict = common.transInfo(bdata)
  
  totalDiffSize = 0
  diffs = []
  for k, v in bdict.items():
    sz = v['S']
    szstr = '{:.2f}M'.format(v['S']/1024/1024)
    if k not in adict:
      totalDiffSize += sz
      diffs.append([k, szstr])
    elif v['H'] != adict[k]['H']:
      totalDiffSize += sz
      diffs.append([k, szstr])
  print('totalDiffSize = {:.2f}M'.format(totalDiffSize/1024/1024))
  if totalDiffSize > 0:
    for v in diffs:
      print(v)

if __name__ == "__main__":
  compare()