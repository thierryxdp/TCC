def total(lista,produtos):
    resultado=0
    for produto in lista:
        
        resultado += produtos[produto]
        
    return resultado