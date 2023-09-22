def total(listacompras,precos):
    '''função que recebe uma lista de compras e um dicionario com o 
    preço de cada produto, e retorna o valor total dos itens.
    entrada:lista,dicionario
    saída:float'''
    
    x=0
    for i in range(len(listacompras)):
        x=x+precos[listacompras]
    return round(p,2)