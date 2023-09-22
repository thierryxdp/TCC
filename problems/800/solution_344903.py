def total(Lista,Dicionario):
    '''retorna valor dos itens da lista disponíveis na loja
    list,dict->float'''
    
    i=0
    
    for Produtos in range (len(lista)):
        CarrinhoCompras=lista[CarrinhoCompras]
        if CarrinhoCompras in dict.keys(Dicionario):
            i=i+dict.get(Dicionario,CarrinhoCompras)
    return round(i,2)