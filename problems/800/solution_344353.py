def total(lista,dicionario):
    '''retorna o preço de uma lista a se comprar
    list,dict->float'''
    
    total_pagar=[]
    
    for item in lista:
        if item in dicionario:
            total_pagar+=(dict.get(dicionario,item),)