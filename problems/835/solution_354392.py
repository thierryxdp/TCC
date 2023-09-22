lista = [ ]
    A = 0
    B= 0
    listaA = 0
    listaB = 0
    for i in matriz:
        
        for j in i:
            lista = lista + [j]
    menor = min(lista)
    
    for i in matriz:
        B = 0
        A = A + 1
        for j in i:
           if menor == j:
              listaB = listaB + B
              listaA = listaA + A
           B = B + 1
    return listaA,menor,listaB+1