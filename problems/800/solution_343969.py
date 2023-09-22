def total(lista_de_compras, produtos):
    valor_final = 0
    
    for item in lista_de_compras:
        if item in produtos:
            valor_final += produtos[item]
            
    return round(valor_final, 2)