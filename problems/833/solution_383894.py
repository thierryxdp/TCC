def conta_numero(numero,matriz):
    contador=0
    for i in matriz:
        if numero in numero[i]:
            contador+=1
        else:
            contador+= 0 
    return contador