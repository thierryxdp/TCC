def eh_quadrada(matriz):
    '''funcao que identifica se uma matriz dada como entrada e quadrada, retornando true se for e false se nao;
       list(list)-> bool'''
    linhas= 0
    coluna= 0
    for i in range(len(matriz)):
        linha = linha+1
        for j in range(len(matriz[i])):
                 coluna= coluna+1
    if linhas == colunas:
         return True
    else:
         return False