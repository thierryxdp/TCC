def total(lista,produtos):
    '''funcao que, dada uma lista de compras e os precos de cada produto, retorna o valor
    que sera gasto ao comprar os itens da lista;
    list(str),dict(str,float)->float'''
    soma=0
    for compra in lista:
        if compra in produtos:
            soma=soma+dict.get(produtos,compra)
    return soma