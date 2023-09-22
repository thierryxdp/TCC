import math

def acima_da_media(notas):
    """Função que dada uma lista de números inteiros nos retorna aqueles que são maiores que a média dos números. 
    list -> list """

    media = math.ceil(sum(notas)/len(notas))

    list.append(notas, media)
    list.sort(notas)

    return notas[list.index(notas, media)+1:]