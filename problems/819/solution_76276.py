def filtraMultiplos(lista,numero):
    """ Recebe uma lista de números e um numero e retorna outra
    lista com todos multiplos do numero presentes na lista de entrada
    list,int -> list
    """
    Multiplos = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%numero == 0:
            Multiplos = Multiplos + [lista[proximo]]
        proximo = proximo + 1
    return Multiplos