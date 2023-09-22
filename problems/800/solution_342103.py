def total(lista,dicionario):
    soma=0
    for i in lista:
        if i in dicionario:
            soma=soma+dicionario[i]
    a=round(soma)        
    return a