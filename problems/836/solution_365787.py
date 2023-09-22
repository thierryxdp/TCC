def busca (setor, matriz):
    """Função que, dado um setor e uma matriz de dados, retorna todos os funcionários daquele setor.
    Entrada: string e lista.
    Saída: lista."""
    
    encontrado = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[0][2] == setor:
                list.append(encontrado, matriz[0])
    return encontrado