def total(lista,produtos):
    
    valor = 0
    for item in lista:
        if item in produtos.keys :
            valor += produtos.get(item)
    return valor