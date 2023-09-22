def filtra_pares(elementos):
    """ Retorna somente os números pares contidos na tupla elementos, que deve conter 4 números inteiros
    tuple -> tuple """
    saida = ()
    if (elementos[0]%2==0):
        saida += (elementos[0],)
    if (elementos[1]%2==0):
        saida += (elementos[1],)
    if (elementos[2]%2==0):
        saida += (elementos[2],)
    if (elementos[3]%2==0):
        saida += (elementos[3],)

    return saida