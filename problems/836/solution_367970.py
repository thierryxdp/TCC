def busca(setor,matriz):
    '''Função que recebe uma string e uma matriz e retorna uma nova 
    matriz com as linhas da matriz original que possuem a string passada'''
    '''str,list(list(str)) --> list(list(str))'''
    i = 0
    j = 0
    M = []
    while i < len(matriz):
        for j in matriz[i]:
            if j == setor:
                matriz[i].pop(2)
            	M.append(matriz[i])
               	
        i = i + 1
    return M