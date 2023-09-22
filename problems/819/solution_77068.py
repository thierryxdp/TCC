def filtraMultiplos(lista:list, numero:int):
    multiplos = list()
    for numero in lista:
        if (numero % 2 ==0):
            multiplos.append(numero)

            return multiplos