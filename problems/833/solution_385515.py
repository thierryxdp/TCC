def conta_numero(numero,matriz):
    '''conta quantas vezes um dado número aparece na matriz; int,list->int'''
    contador=0
    for i in matriz:
        for j in i:
            if j==numero:
                contador+=1
                
    return contador