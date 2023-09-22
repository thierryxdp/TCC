def conta_numero(numero,matriz):
    """funcao que retorna a quantidade de vezes que um numero aparece em uma matriz de numeros inteiros;
    int,list(list) -> int"""
    c = 0
    n = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            c = +1
            if numero ==  matriz[i][j]:
                n+=1
                

    return n