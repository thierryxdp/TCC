def repetidos(lista):
    contador=0
    aux=0
    for n in lista:
        contador += 1
        if contador < len(lista):
            if n == lista[contador]:
                aux +=1
    return aux