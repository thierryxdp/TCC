def total(lista,dicionario):
    soma=0
    for i in lista:
        if i in dict.keys(dicionario):
            soma=soma+dicionario[i]
        return soma