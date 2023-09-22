def busca (setor, matriz):
    """Funcao que receba uma matriz e faz uma busca dado setor que retorna os dados de todos os funcionarios daquele setor"""
    copia = matriz.copy()
    linhas = len(matriz)
    matriz_f = []
    for i in range(linhas):
        if setor in matriz[i]:
             matriz[i].remove(setor)
             matriz_f.append(matriz[i])
        else:
            pass
    return matriz_f