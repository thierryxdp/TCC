def conta_numero(numero,matriz):
    cont=0
    soma=0
    while cont<len(matriz):
     for n in matriz[cont]:
         if n==numero:
            soma+=1
     cont+=1
    return soma