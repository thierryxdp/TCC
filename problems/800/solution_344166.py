def total(lista,dic):
    '''dada uma lsita de compras e um dicionário com os preços de cada produto
    disponível, retorna o valor total dos itens da lsita que estejam disponíveis
    list,dict->float/int'''
    valor=0
    for produto in  range(len(l)):
        x = lista[produto]
        if x in dict.keys(dic):
            valor+=dict.get(dic,x)
    return round (valor,2)