# Filtramultiplos



def filtraMultiplos(lista,n):
    """essa funcao recebe uma lista e um numero e filtra na lista os numeros que sao divisiveis por n
    list -> list"""
    multiplos = []
    for i in range(len(lista)):
        if lista[i]%n == 0:
            multiplos.append(lista[i])
    return (multiplos)


#filtraMultiplos([20,22,11,7,19,26,8,18,29,28,13,15,10],6)