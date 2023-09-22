def conta_numero(numero,matriz):
    i=0
    vezes=0
    while i<len(matriz):
     for n in matriz[i]:
         if n==numero:
            vezes+=1
     i+=1
    return vezes