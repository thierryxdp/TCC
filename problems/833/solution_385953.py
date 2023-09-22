def conta_numero(num,matriz):
    contador=0
    i=0
    for x in matriz:
        contador= contador+ list.count(matriz[i],num)
        i=i+1
        return contador