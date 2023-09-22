# 
#
#
#
def total(lista,dicionario):
    i=0
    
    while i<len(lista):
        if lista[i] in dicionario:
            tot=dict.values(lista[i])
        i=i+1
        return tot