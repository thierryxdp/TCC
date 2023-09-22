def busca(setor, matriz):
    '''função que busca em uma matriz de dados, o(s) funcionário(s) correspondentes ao setor de entrada; str, list(lists) -> list'''
    
    resultado = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor in matriz[i]:
                resultado.append(matriz[i])
                
    return resultado