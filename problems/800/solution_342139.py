def total(lista, produtos):
    '''recebe uma lista de compras e um dicionario com o preço de
    cada produto disponível numa loja e retorna o valor total dos 
    itens da lista que estejam disponíveis;
    list,dict->float'''
    valores=[]
    for item in lista:
        list.append(valores,produtos[item])
    return round(sum(valores),2)