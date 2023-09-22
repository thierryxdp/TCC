def total(lista, preco):
    '''retorna o valor total a ser pago de acordo com a lsta de compra e os precos tabelados;
    list,dict->float'''
    valor=0
    for produto in lista:
        if produto in preco:
            valor=valor+preco[produto]
    return round(valor,2)