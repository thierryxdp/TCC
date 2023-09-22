# 
#
#
#
def total(lista,dicionario):
    i=0
    tot=0
    while i<len(lista):
        if lista[i] in dicionario:
            tot=tot+dict.values(lista[i])
        i=i+1
    return tot