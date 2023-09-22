def melhor_volta(matriz):
    """dada o tempo das voltas de uma corrida, retorna quem 
    quem teve a melhor volta, o tempo e qual foi a volta.
    matriz--->tupla"""
    tempo=[]
    corredor=[]
    quantidade=len(matriz)
    for var in range(quantidade):
        menor_tempo=min(matriz[var])
        list.append(tempo,menor_tempo)
        for x in range(len(menor_tempo)):
            dados=[]
            if melhor_tempo==((matriz[var])[x]):
                list.append(dados,x)
                list.append(corredor,dados[0])
    primeiro_tempo=min(tempo)
    primeiro_corredor=corredor[tempo.index(primeiro_tempo)]
    return (((tempo.index(primeiro_tempo)+1),primeiro_tempo,(primeiro_corredor+1)))