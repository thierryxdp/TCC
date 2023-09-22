def conta_numero(procura,matriz):
    i, j = 0,0
    for procura in matriz:
        if procura in matriz:
            j = matriz.index(procura)
            break
        i+=1
        return i