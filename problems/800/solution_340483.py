def total (produtos, precos):
    '''retorna o valor total dos itens da lista'''
    '''list,dici -> float'''
    
    lista=[]
    for produto in produtos:
        if precos in produtos[produto]:
            lista= lista + [produto]
	return lista