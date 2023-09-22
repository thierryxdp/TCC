def filtraMultiplos(lista,n):
    ''' essa função tem como entrada uma lista e um numero, e  retorna uma lista com os numeros da lista original só que com os numeros divisiveis por n'''
    multiplos = []
    for multiplos in lista:
        if multiplos%n == 0:
            return lista.append(multiplos)