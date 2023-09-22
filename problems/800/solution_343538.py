def total(compras,preco):
    '''função que dado uma lista de compras verifica se tem o item 
    no dicionario e retorna o custo da compra
    ass: list, dict --> float    '''
    i=0
    a=list(dict.keys(preco))   
    soma=0
    
    while i<len(compras):
        if compras[i] in a:
        soma=preco[compras[i]]
        
    return soma