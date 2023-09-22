def total(lista,dicio):
    '''
    funcao que recebe uma lista de compras e um dicionario
    contendo o preco de cada produto disponivel e retorna o valor 
    total dos itens da lista que estao disponiveis
    list,dicio -> float
    '''
    i = 0
    contador = 0
    while (i<len(lista)):
        if lista[i] in dicio:
            contador = contador + dicio[lista[i]]
        i += 1
        

    return round(contador,2)