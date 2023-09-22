def busca(setor, matriz):
    '''essa funçao recebe uma matriz e faz uma busca por setor, retornando todos os dados dos 
    funcionarios daquele setor
    str, list -> list'''
    lista=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==setor:
                copia=list.copy(matriz[i])
                list.pop(copia,j)
                list.append (lista, copia)
    return lista