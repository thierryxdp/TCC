def conta_numero (numero,matriz):
    '''função que dado um número inteiro e uma matriz, 
    de inteiros, de qualquer tamanho retorna quantas vezes
    o número dado apareceu na matriz
    int,list -> int'''
    
    contador = 0
    
    for i in range(len(matriz)):
        for j in matriz[i]:
            if j == numero:
                contador +=1
    return contador