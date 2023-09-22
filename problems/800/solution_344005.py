def total(lista_de_compras, produtos):
    valor_final = 0
    
    for x in lista_de_compras:
        if x in produtos:
            valor_final += produtos[x]
            
    return valor_final + float(0,1)