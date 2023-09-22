def busca(setor,matriz):
    '''recebe uma matriz com o nome dos funcionário, o registro, o setor e o número de telefone e o setor a ser identificado. Com isso, dado o nome do setor, retorna os dados de todos os funcionários daquele setor; str,list -> list'''

    aux = [] 
    
    for i in range(0,len(matriz)):
        if matriz[i][2] == setor:
            aux.append([matriz[i][0],matriz[i][1],matriz[i][3]])

    return aux