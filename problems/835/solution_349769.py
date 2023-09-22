def melhor_volta(matriz): #Refazer
    '''Retorna qual dos 6 corredores teve a melhor volta da prova de 10 voltas
list -> str'''
    linhas=len(matriz)
    colunas=len(matriz[0])
    min_individual=[]
    for i in range(linhas):
        min_individual=min_individual+min(matriz[i])
    min_coletivo=min(min_individual)
    for i in range(linhas):
        for j in range(colunas):
            if min_coletivo in matriz[i][j]:
                melhor_corredor=matriz[i]
                melhor_volta=matriz[i][j]
    return melhor_corredor,min_coletivo,melhor_volta