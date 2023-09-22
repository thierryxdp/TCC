def total(lista_compras,precos):
    """funcao que recebe uma lista com produtos desejados e um dicionario com os precos de uma loja e retorna o valor total da compra;
       list,dict->float"""
    total_compra=0
    for i in range(len(lista_compras)):
        if lista_compras[i] in precos:
            total_compra=total_compra+precos[lista_compras[i]]
    return total_compra