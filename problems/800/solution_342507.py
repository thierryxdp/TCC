def total(lista_compras,dicionario_precos):
    '''retorna o valor da lista de compras através do dicionario de precos informado.list,dic->float'''
    soma=0
    for i in lista_compras:
        preco=dicionario_precos[i]
        soma=preco+soma
    return round(soma,2)