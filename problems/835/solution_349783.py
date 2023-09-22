def melhor_volta(matriz): #Refazer
    '''Retorna qual dos 6 corredores teve a melhor volta da prova de 10 voltas
list -> str'''
    linhas=len(matriz)
    colunas=len(matriz[0])
    min_individual=[]
    for i in range(linhas):
        min_individual=min_individual+[min(matriz[i])]
    min_coletivo=min(min_individual)
    for i in range(1,linhas+1):
        for j in range(1,colunas+1):
            if min_coletivo==matriz[i][j]:
                melhor_corredor=i
                melhor_volta=j
    return melhor_corredor,min_coletivo,melhor_volta