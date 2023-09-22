def total(lista,produtos):
    '''função responsável por comparar os itens de uma lista de compras à um dicionário que possui os itens disponíveis e seus valores, para assim retornar o valor dos itens da lista de compras disponíveis naquele mercado
lista=lista de compras 
produtos=dicionário contendo os produtos disponíveis e valores'''
    total=0
    for i in lista:
        if i in produtos:
            total=total+produtos[i]
    return round(total,2)