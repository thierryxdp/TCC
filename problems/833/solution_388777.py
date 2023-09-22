def conta_numero(numero,matriz):
    posi=0
    cont=0
    while posi< len(matriz):
        posi2=0
        while posi2< len(matriz[posi]):
            if matriz[posi][posi2]==numero:
                cont+=1
            posi2+=1
        posi+=1
    return cont