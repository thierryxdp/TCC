def total(lista,dicionario):
    x=0
    j=[]
    while x <len(lista):
        if lista[x]in dicionario:
            j = j + dicionario[x]
            i = i + 1
            return j