def total(lista, itens):
    ''' Função que recebe uma lista de compras e retorna o preço
    total a ser pago'''
    'list,dict--->float'
    i=0
    x=len(lista)
    y=len(itens)
    resultado=dict.values(itens)
    produto=dict.keys(itens)
    preco=int()
        
    while  i < x:
        if  lista[i] in itens :
            achei=(itens[lista[i]])
            preco=preco+achei
           
        i=i+1
    return (preco)