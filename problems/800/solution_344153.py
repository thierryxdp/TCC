def total(lista,preco):
    '''retorna o valor total dos iteis da lista que estão disponíveis;
list,dict->float'''
    valor=0
    
    for i in lista:
        if lista[i] in preco:
            valor=valor + preco[lista[i]]
            
    return round(valor,2)