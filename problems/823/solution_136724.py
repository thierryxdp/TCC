def faltante(ls):
    ''' Função que da o número faltante de 1 a N da lista dada.
    list -> int'''
    cont = 0
    lista = sorted(ls)

    while cont < len(ls):
        if cont + 1 == lista[cont]:
            cont += 1

        else:
            return cont + 1

    return cont + 1