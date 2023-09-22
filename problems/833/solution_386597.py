def conta_numero(numero,matriz):
    '''Essa funcao recebe de entrada um numero inteiro e 
    uma matriz de inteiros de tamanho qualquer e retorna 
    quantas vezes esse numero aparece na matriz.
    int, matriz (int) -> int'''
    
    qtd = 0
    
    if len(matriz) == 0:
        return qtd

    for linha in matriz:
        for n in linha:
            if n == numero:
                qtd += 1
    return qtd

#Casos teste
# matriz = [[2,2,2],[2,2,2],[2,2,2]]
# conta_numero(2, matriz) == 9

# matriz2 = [[0,34,55,23],[-2,4,-10,-10],[-12,-10,76]]
# conta_numero(-10,matriz2) == 3

# conta_numero(5,[]) == 0