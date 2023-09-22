def total(lista,dicionario):
    ''' '''
    for produto in dicionario:
        valor=dicionario[produto]
        valor += valor
    return valor