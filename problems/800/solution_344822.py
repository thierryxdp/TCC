def total(lista,preco):
    '''funcao que recebe uma lista de compras com o preço de cada produto e devolve
    seu valor total list,dic->int'''
    precos=[]
    for i in lista:
        if i in dict.keys(preco):
            precos.append(preco[i])
    return round(sum(precos),2)