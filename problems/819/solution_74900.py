def filtraMultiplos(listadenumeros,n):
    multiplos = []
    proximo = 0
    while proximo<len(listadenumeros):
          if listadenumeros[proximo]%n == 0:
                multiplos = multiplos + (listadenumeros[proximo])
                proximo = proximo + 1
    return multiplos