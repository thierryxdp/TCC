def total(lista, dicionario):
    """ Dados uma lista de compras e um dicionário com o preço de produtos de uma loja, reorna o volor total dos itens da lista que tenham na loja;
    list, dict->float """
    i=0
    lista2=[]
    for i in range(len(lista)):
         if lista[i] in dicionario:
             lista2=lista2+[dicionario[lista[i]]]
            
         i=i+1
    return round(sum(lista2),1)