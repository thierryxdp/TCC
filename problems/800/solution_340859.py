def total(lista,dicionario):
    x=0
    soma=0
    for elemento in dicionario:
        if lista[x] in dicionario:
            soma= soma+ dicionario[elemento]
            return soma