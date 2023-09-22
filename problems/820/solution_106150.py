def posLetra(string='',letra='',num=0):
    if (string.count(letra)>=num):
        lista=list(string)
        for i in range(num-1):
            numb=int(lista.index(letra))
            lista[numb]=''
        string=''.join(lista)
        return string.index(letra)
    return -1