def total(lista,dici):
    'descrição'
    for i in lista:
        if dici[i] in dici:
            return 'tem'
        else:
            return 'n'