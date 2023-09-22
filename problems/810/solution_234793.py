def inverte(texto):
    sep = list(str.split(texto," "))
    return range(sep[-1],sep[0],-1)