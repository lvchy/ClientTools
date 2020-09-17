_seed = 131

def bkdrhash(str):
    hashnum = 0
    sz = len(str)
    for i in range(sz):
        hashnum = (hashnum * _seed) + ord(str[i])
    
    return hashnum & 0x7FFFFFFF

if __name__ == "__main__":
    print(bkdrhash('hello world'))