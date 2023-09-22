def multiplos(lista, numero):
    """Funcao que recebe uma lista de numeros e um numero inteiro e a partir
    	disso verifica quais numeros da lista sao multiplos do numero indicado"""
    multiplos = []
    contador = 0
    while contador < len(lista):
        if lista[contador] % numero == 0:
            list.append(multiplos, lista[contador])
        contador += 1
    return multiplos