def filtraMultiplos(lista,num):
    """essa função recebe uma list de numeros e retorna uma outra lista com seus multiplos
    Entrada lista e saida lista"""
    i=0
    multiplos = []
    while i < len(lista):
        if lista[i]%num == 0:
            multiplos.append(lista[i])
        i=i+1
    return multiplos