def total(lista, dic):
    '''funcao que recebe uma lista e um dicionario retorna o valor total dos intens da lista que estejam disponiveis nesta loja
    list,dict->int'''
    valor=0
    for produto in range(len(lista)):
        y = lista[produto]
        if y in dict.keys(dic):
            valor+=dict.get(dic,y)
    return round(valor,2)