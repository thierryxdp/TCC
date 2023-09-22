# a funcao retorna os numeros que sao multiplos de um numero dado
#list, int->list
def filtraMultiplos(l, n):
    multiplos = []
    for val in l:
        if val%n==0:
            multiplos.append(val)
    return multiplos