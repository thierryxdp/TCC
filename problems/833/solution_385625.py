def conta_numero(numero,matriz):
    if matriz==[]:
        return 0
    if len(matriz[0])==len(matriz):
         return list.count(matriz[0],numero)