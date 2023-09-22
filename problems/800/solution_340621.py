def total (lista, dicio):
    '''
    	 essa função recebe uma lista de compras e retorna o valor total
         das compras caso haja os produtos em uma determinada loja com os
         valores presentes no dicionário
         list, dict-> valor
    '''
    i = 0
    x = []
    for i in range(len(lista)):
        if lista[i] in dicio:
            x.append(dicio[lista[i]])
            i = i+1
        else:
            i = i+1
    return round(sum(x), 2)