def total2(lista, dicionario):
    """ Dados uma lista de compras e um dicionário com o preço de produtos de uma loja, reorna o volor total dos itens da lista que tenham na loja;
    list, dict->float """
    lista2=[]
    for i in lista:
         if i in dicionario:
             lista2=lista2+[dicionario[i]]
    return round(sum(lista2),2)