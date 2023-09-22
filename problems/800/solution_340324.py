def total(lista,dicionario):
    '''retorna o preço de uma lista a se comprar'''
    
    total_pagar=[]
    
    for item in lista:
        if item in dicionario:
            total_pagar+=round((dict.get(dicionario,item)),2)
            
    return sum(total_pagar)