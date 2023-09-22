def melhor_volta(m):
    """
    Função que recebe uma matriz 6x10 contendo os tempos de 6 corredores em cada uma das 10 voltas na corrida e retora uma tupla contendo o número do corredor(de 1 a 6) que conseguiu a melhor volta, o tempo dessa volta e o número dela(de 1 a 10).
    Parâmetro:
    	m: list
    Saída:
    	tuple
    """
    #lista com as voltas do menor tempo de cada corredor.
    melhores_voltas = []
    #lista com número de ordem (1 a 10) da volta do menor tempo de cada corredor.
    ordem_melhor_volta = []
    for i in range(len(m)):
        melhores_voltas.append(min(m[i]))
        ordem_melhor_volta += [m[i].index(min(m[i]))]
    #menor tempo de volta dentre todos os corredores.
    melhor_volta = min(melhores_voltas)
    #número de ordem (0 a 5) do corredor com a volta do menor tempo dentre todos os corredores.
    melhor_corredor = melhores_voltas.index(min(melhores_voltas))
    melhor_volta_melhor_corredor = ordem_melhor_volta[melhor_corredor]
    return melhor_corredor+1, melhor_volta, melhor_volta_melhor_corredor+1