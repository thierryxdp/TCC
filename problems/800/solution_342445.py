def total (lista,precos):
    '''A função recebe dois parametros de entrada, uma lista de compras
    	e uma da tabela de itens e preços, faz uma varredura nos preços
        determinando os valores dos itens da lista e retorna o total;
        list, dict --> int
   	'''
    lst = []
    for i in lista:
        lst.append(precos[i])

    return round(sum(lst),2)