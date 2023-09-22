def total(lista,dicionario):
    '''Uma função que calcula qual o valor total da soma dos itens
    de uma lista dado um dicionario
    list, dici -> float'''
    
    total = 0
    for i in lista:
        if i in dicionario:
        	total += dicionario[i] 
    return round(total)