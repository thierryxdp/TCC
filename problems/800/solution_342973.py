def total(lista,dicionario):
    ''' '''
    for produto in lista:
        valor=dicionario[produto]
        valor += valor
        valor= round(valor,2)
    return valor