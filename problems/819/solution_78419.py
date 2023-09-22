def filtraMultiplos(lista,n):
    acumulador = []
    i = 0
    while i < len(lista):
        if lista[i]%n != 0:
            i = i + 1
            acumulador = acumulador
        else:
            acumlador.append(lista[i])
            i = i + 1