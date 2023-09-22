def total(lista,dicionario):
    ''' '''
    valor = 0
    for produto in dicionario:
        valor=dicionario[produto]
        valor += valor
    return valor