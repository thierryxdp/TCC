def total(lista,dicionario):
    ''' '''
    for produto in lista:
        valor=dicionario[produto]
        valor += valor
    return round(valor,2)