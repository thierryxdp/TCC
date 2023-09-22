def melhor_volta(matriz: list)-> tuple:
    """Dada uma matriz 6 x 10 cujas linhas representam seis
    corredores de uma pista de Kart e as colunas contêm os tempos
    em que realizaram uma volta na pista(cada corredor corre 10
    voltas), retorna quem teve a melhor volta, qual foi o tempo
    dela e em que volta ocorreu."""

    melhores_voltas = []
    voltas = []

    for i in range(6):
        list.append(melhores_voltas,min(matriz[i]))
        list.append(voltas, list.index(matriz[i],min(matriz[i])))
        
    melhor_volta = min(melhores_voltas)
    num_volta = voltas[list.index(melhores_voltas,melhor_volta)] + 1
    corredor = list.index(melhores_voltas,melhor_volta) + 1

    return (corredor,melhor_volta,num_volta)