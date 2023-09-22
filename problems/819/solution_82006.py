def filtraMultiplos(listaNum, num):
    multiplos = []
    for elemento in listaNum:
        if elemento%num == 0:
            multiplos.append(elemento)
    return multiplos