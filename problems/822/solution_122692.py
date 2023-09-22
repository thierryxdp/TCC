def repetidos(listaNum):
    anterior = listaNum[0]
    repetidos = 0
    for num in listaNum[1:]:
        if num == anterior:
            repetidos += 1
        anterior = num
    return repetidos