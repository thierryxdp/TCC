def total(lc, d):
    '''Calcule e retorne uma função que receba uma lista de compras e 
    um dicionario que contem o preço dos itens'''
    
    r = []
    for i in lc:
        if i in d:
            list.append(r, (dict.get(d,i)))
    r = sum(r)
    r = round(r,2)
    
    return r