f = frase
    pa = palavra
    po = posicao
    f2 = f.split()
    if pa in f2:
        list.insert(f2,list.index(f2,pa),pa.upper())
        return (' '.join(f2[0:list.index(f2,pa)] + f2[list.index(f2,pa)+1:]))
    else:
        f3=f.split()
        list.insert(f3,po,pa)
        return (' '.join(f3))