def repetidos(lista):
    """Dado uma lista, mostra quantos números repetido em sequência tem na lista. list>int"""
    i=0
    res=0
    while i<(len(lista)-1):
        if lista[i]==lista[i+1]:
            res+=1
        i+=1
    return res