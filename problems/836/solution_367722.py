def busca(nome,matriz):
    """Dada um nome de setor e uma matriz com
    as informações dos funcionários da empresa
    retorna as informações daquele funcionário
    daquele setor correspondente ."""
    copia = matriz.copy()
    linhas = len(matriz)
    resultado = []
    for i in range(linhas):
        if setor in matriz[i]:
            matriz[i].remove(setor)
            resultado.append(matriz[i])
        else:
            pass
    return resultado