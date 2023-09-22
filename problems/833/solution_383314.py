def conta_numero(numero,matriz):
    ''' usando a função range para saber o início da string e o
    len para saber quantos caractéris, assim depois de saber o tamanho,
    precisamos saber onde começa, termina e determinar o a quatidade de vezes
    que o número aparece'''
    T=0
    for l in range(len(matriz)):
        for i in range(len(matriz[0])):
            if matriz[l][i]==numero:
                T+=1
    return T