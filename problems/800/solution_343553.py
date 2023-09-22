def total(lista_de_compras, inventario):
    '''funcao que recebe uma lista de compras e um inventario no que está presente na loja e retorna o valor total dos produtos disponiveis
       list, dic -> int'''
    i=0
    valor=0
    while i<len(lista_de_compras):
        if lista_de_compras[i] in dict.keys(inventario):
            valor= round((valor + dict.get(inventario,lista_de_compras[i]),2)
        i=i+1
    return valor