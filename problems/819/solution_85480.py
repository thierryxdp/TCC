def filtraMultiplos(multiplos, num):
    #função chamada filtraMultiplos para filtrar os múltiplos de um número n.; lista(int) => int#
    m = []
    for i in range(0, len(multiplos)):
        if(multiplos[i] % num == 0):
            m.append(multiplos[i])
        i=i+1
    return m