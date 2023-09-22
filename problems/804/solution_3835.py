def filtra_pares(tupla):
    """Dada uma tupla com quatro elementos inteiros, retorna uma nova tupla
       com apenas os elementos pares da tupla original """
    par = ()
    if tupla [0]%2 == 0:
        par = par + (tupla[0], )
    elif tupla [1]%2 == 0:
        par = par + (tupla[1], )
    elif tupla [2]%2 == 0:
        par = par + (tupla[2], )
    elif tupla [3]%2 == 0:
        par = par + (tupla[3], )