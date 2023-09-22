def repetidos(lista):
    i = 0
    contador = 0
    anterior,valor=-1,-1
    while i<len(lista):
        valor=lista[i]
        if valor==anterior:
            contador=contafor+1
        anterior=valor
        i=i+1
    return contador