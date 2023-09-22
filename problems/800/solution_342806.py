def total(lista_compra,produtos_loja):
    """Essa função retorna o valor de uma compra, dado uma
    lista de compras e um dicionario com os valores de cada 
    produto de uma loja
    lista,dicionario - > float """
    compra = 0.0
    
    for i in range(len(lista_compra)):
        compra = compra + produtos_loja[lista_compra[i]]
    
    return  round(compra,2)