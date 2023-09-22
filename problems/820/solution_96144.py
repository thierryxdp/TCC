def posLetra(string,letra,n):
    str.replace(string,letra,'1',n-1)
    return str.find(string,letra)