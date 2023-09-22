def filtraMultiplos(lista,n):
    """Função que acha os valores multiplos do numero dado.
    parametros: lista,numero->lista"""
    multiplos = list()
    indice = 0
    while indice < len(lista):
        if lista[indice]%n == 0:
            multiplos.append(lista[indice])
        indice = indice +1
    return multiplos