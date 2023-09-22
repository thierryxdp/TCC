def filtraMultiplos(listadenumeros,n):
    """A função filtraMultiplos, como o nome indica, informará quais são os múltiplos de um
    número contidos numa lista, sendo que ambos devem ser informados na entrada. Como resultado,
    teremos a lista de múltiplos."""
    multiplos = []
    proximo = 0
    while proximo<len(listadenumeros):
          if listadenumeros[proximo]%2 == 0:
             multiplos = multiplos + [listadenumeros[proximo],]
          proximo = proximo + 1
    return multiplos