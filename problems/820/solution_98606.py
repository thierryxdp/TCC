def posLetra(string,letra,num):
    '''str, str, inr -> str'''
    i = 0
    indice = 0
    while i<len(string):
        x = str.find(string,letra)
        indice = indice + x
        i = i + 1
    return indice