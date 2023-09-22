def busca(dado,matriz): #Refazer
    '''Retorna as informações dos funcionários que possuem o dado informado
str,list -> list'''
    linhas=len(matriz)
    colunas=len(matriz[0])
    funcionarios=[]
    for i in range(linhas):
        for j in range(colunas):
            if dado==matriz[i][j]:
                matriz[i].del(2)
                funcionarios=funcionarios+matriz[i]
    return funcionarios