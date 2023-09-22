def total (lista_compras, produtos):
    ''' Função que recebe uma lista de compras e um dicionário contendo 
    cada produto preço com seu respectivo preço e que retorna o valor toal 
    dos produtos presentes na lista
    list, dict -> float'''
    numero = 0
    for indice in lista_compras:
        if indice in produtos:
            numero= numero + produtos[indice]
            valor_total= round(numero, 2)
        return valor_total