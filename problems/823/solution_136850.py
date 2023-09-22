def faltante(listaNum):
    listaNum.sort()
    Max = listaNum[-1]
    intervalo = list(range(1, Max + 1))
    
    if listaNum == intervalo:
        return Max + 1
    
    for n in intervalo:
        if n not in listaNum:
            return n