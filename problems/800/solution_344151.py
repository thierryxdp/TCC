def total(lista,preco):
    '''retorna o valor total dos iteis da lista que estão disponíveis;
list,dict->float'''
    valor=0
    i=0
    
    for produtos in lista:
        if lista[i] in preco:
            valor=valor + preco[lista[i]]
            i=i+1
    return round(valor,2)