def conta_numero(numero,matriz):
    """Para cada valor de 0 até o tamanho da matriz, é verificado para 
    cada valor de 0 até o tamanho dos elementos da matriz, se o número
    é igual. Ou seja, a função substitui 'matriz[i][j]' todos valores
    possíveis de 'i' e 'j' que se mantenham em um índice possível.
    Caso o número seja o mesmo, soma a constante que começa com o valor de 0
    mais 1. Ao final retorna a constante, que terá o número de vezes
    que o número apareceu.
    int, lista -> int
    """
    vezes=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero==matriz[i][j]:
                vezes+=1
    return vezes