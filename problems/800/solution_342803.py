def total(lista_compra,produtos_loja):
    """ 
    lista,dicionario - > float """
    compra = 0.0
    
    for i in range(len(lista_compra)):
        
        compra = compra + produtos_loja[lista_compra[i]]
    return compra