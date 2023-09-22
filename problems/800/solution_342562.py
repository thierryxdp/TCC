def total(listacompra,produtos):
    '''função que dada uma lista de compra e produtos disponiveis
    em determinada loja, retorna o valor total dos itens
    que estao na lista de compras e estao disponiveis nos produtos
    list,dicionario -> float'''
    
    somatotal = 0
    
    for produto in listacompra:
        if produto in produtos:
            somatotal = somatotal + produto
    return round(somatotal,2)