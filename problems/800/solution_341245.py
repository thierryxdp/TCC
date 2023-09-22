def total(lista, dicionario):
    ''' funcao que retorna o valor, contido em 
    um dicionario, dado um indice em uma lista
    entrada: lista, dincionario 
    saida: float
    '''
    valor_total= 0
    indice= 0
    while indice<len(lista):
        if lista[indice] in dicionario:
            valor = dicionario[(lista[indice])]
        valor_total= valor_total + float(valor) 
        indice= indice + 1
        
    return round(valor_total, 2)