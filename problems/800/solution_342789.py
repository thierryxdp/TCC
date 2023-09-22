def total(lista_compras,dicionario_produtos):
    resultado = 0
    for produto in lista_compras:
        resultado += dicionario_produtos[produto]
        resultado = round(resultado,2)
    return resultado