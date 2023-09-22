def conta_numero(numero,matriz):
    ''' Função que retornar quantas vezes o numero foi repetido 
        matriz.
        int,list(list)--->>int'''
    x=0
    ma=0
    for i in range(len(matriz)):  
        for j in range(len(matriz[-1])):
            ma=matriz[i][j]
            if ma == numero:
                x+=1
        
    return x