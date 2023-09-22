def total(lista,dicionario):
    '''
    função que recebe como entrada uma lista de compras e 
    um dicionário com o preço de cada produto de uma loja. 
    O retorno será o valor total dos itens da lista que 
    estejam disponíveis nesta loja.
    list, dict -> float
    '''
    valor_inicial = 0
    posicao = 0
    
    for posicao in lista:
        if lista[posicao] in dict.keys(dicio):
            valor_inicial = valor_inicial + dict.get(dicionario, lista[posicao])
        posicao = posicao + 1
        
    return round(valor,2)