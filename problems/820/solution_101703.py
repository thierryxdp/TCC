def posLetra(frase,letra,ocor):
    lista = list(frase)
    m = 0
    cl = 0
    final1 = 0
    while m < len(lista):
        if lista[m] == letra:
            cl = cl + 1
            m = m + 1
            if cl == ocor :
                final1 = m
        else:
            m = m + 1

    if lista[final1 - 1] == letra:
        return final1 - 1
    else:
        return -1