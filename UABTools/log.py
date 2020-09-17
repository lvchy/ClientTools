import utfile

outs = []
def log(*args):
    s = ''
    for arg in args:
        s += str(arg)+'|'
    outs.append(s[:len(s)-1])

def save(path):
    utfile.writeToFile(path, '\n'.join(outs))