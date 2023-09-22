def acima_da_media(notas):
    """Função que ao receber uma lista com notas, retorna outra lista
    com notas que estão acima da média;
    list -> list"""
    n = sum(notas)/len(notas)
    notas[0:0] = [n]
    list.sort(notas)
    x = list.index(notas,n)
    if n == notas[x+1]:
        return notas[x+2:]
    else:
        return notas[x+1:]