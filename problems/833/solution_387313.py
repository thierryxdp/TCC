def conta_numero(numero,matriz): 
    '''dado um nuumero int e matriz de int conta e retorna quantas vezes o numero aparece '''
    contagem=0
    for lista in matriz:
        contagem+=list.count(lista,numero)
    return contagem