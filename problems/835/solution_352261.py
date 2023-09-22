def melhor_volta(matriz):
    #define o valor minimo da matriz
    minimo = min(matriz[0])
    #define a variavel linha como 0
    linha = 0
    # define a variavel coluna como 0
    coluna = 0
    #percorre cada linha da matriz
    for i in matriz:
        #verifica se o valor minimo da linha é menor do que os ja vistos
        if min(i) < minimo:
            # caso seja menor, define o valor minimo como o sendo o menor encontrado
            minimo = min(i)
            #define a coluna como sendo a posição do numero menor
            coluna = i.index(minimo)
            #define a linha como a posição da lista do menor numero na matriz
            linha = matriz.index(i)
     #retorna tupla com as coordenadas e o valor minimo
    return ([linha,coluna],minimo)