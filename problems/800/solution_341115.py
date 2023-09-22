def total(lista,cardapio):
    """recebe uma lista de compras e o preços dos
    produtos, retornando o valor total dos itens da 
    lista que estejam disponiveis"""
    dispo=[]
    for produto in lista:
        if dict.get(cardapio,produto,0)!=0:
            list.append(dispo,dict.get(cardapio,produto))
    return round(sum(dispo),2)