def eh_quadrada(matriz):
    '''funcao que identifica se uma matriz dada como entrada e quadrada, retornando true se for e false se nao;
       list(list)-> bool'''
    linha= 0
    coluna= 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            linha = linha+1
            coluna= coluna+1
    if linha == coluna:
         return True
    else:
         return False