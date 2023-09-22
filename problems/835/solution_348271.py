def melhor_volta(matriz):

    menor_tempo=999
    corredor=0
    volta=0

    for index,linha in enumerate(matriz):
        tempo=min(linha)
        if tempo < menor_tempo:
            menor_tempo=tempo
            corredor=index+1

    for linha in matriz:
        for indice,coluna in enumerate(linha):
            if coluna==menor_tempo:
                volta=indice+1

    return (corredor,menor_tempo,volta)