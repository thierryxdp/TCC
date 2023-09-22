def filtraMultiplos(lista,numero):
    divisiveis = []
    for i in lista:
        resto = i % numero
        if resto == 0:
            list.append(divisiveis,i)
    return divisiveis