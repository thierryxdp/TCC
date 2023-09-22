def filtraMultiplos(lista,num):
    """Filtra Multiplos de um número N. Lista,int-->Lista """
    diviziveis = []
    for i in lista:
        if i%num==0:
            diviziveis.append(i)
    return diviziveis