def busca (setor, matriz):
    """Função que, dado um setor e uma matriz de dados, retorna todos os funcionários daquele setor.
    Entrada: string e lista.
    Saída: lista."""
    
    encontrado = []
    x = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[x][2] == 'setor':
                list.append(encontrado, matriz[x][2])
        x = x + 1
    return encontrado