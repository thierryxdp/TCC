def total(lista, dicionario):
    soma = 0
    
    for i in lista:
        if(i in dicionario):
            soma += dicionario[i]
    return round(soma, 2)