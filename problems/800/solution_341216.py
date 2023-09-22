def total(lista,produtos):
    
    valor = 0
    for item in lista:
        valor += produtos.get(item)
    return valor