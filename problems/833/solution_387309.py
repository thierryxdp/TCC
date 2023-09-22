def conta_numero(numero,matriz):
    '''retorna quantas vezes o numero aparece na matriz
    int,matriz->int'''
    a=0
    for i in range(len(matriz)):
       
        for j in range(len(matriz[i])):
            if numero==matriz[i][j]:
                a+=1
      
            
    return a