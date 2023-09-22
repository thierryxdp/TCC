def filtraMultiplos(lista, numero):
    """Funcao que filtra os multiplos de um numero tendo como entrada uma lista de
    numeros inteiros e um numero inteiro."""
    multiplos = []
    contador = 0
    while contador < len(lista):
        if lista[contador] % numero == 0:
            list.append(multiplos, lista[contador])
        contador += 1
    return multiplos