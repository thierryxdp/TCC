def total(compras,preco):
    '''funcao que dada uma lista de compras e os precos de todos os produtos em determinada loja, retorna a soma do valor dos itens da lista de compra disponiveis nessa loja;
       list, dict-> float'''
    totalcompras= 0
    for produto in compras:
        if compras[produto] in preco:
            totalcompras= totalcompras + dict.get(preco,compras[produto])
        
    return totalcompras