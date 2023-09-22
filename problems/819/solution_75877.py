def filtraMultiplos(lista,n):
    cont = 0 
    divisíveis = []
    while cont < len(lista):
        if lista[cont]%n == 0:
            divisíveis = divisíveis + lista[cont]
        cont = cont + 1
    return divisíveis