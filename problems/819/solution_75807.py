def filtraMultiplos(lista, n):
    """Retorna uma lista apenas com os multiplos de n que estao na lista dada;
       Entrada:
       Saida:
    """
    multiplos = list()
    contador = 0
    while (contador <len(lista)):
        if (lista[contador]%n ==0):
            lista.append(lista[contador])
        contador = contador+1
    return list(multiplos)