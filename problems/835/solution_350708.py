def melhor_volta(matriz):
    'Dada uma matriz composta pelos tempos em segundos dos corredores em cada volta, retorne quem obteve a mehor prova e tambem com qual tempo e que volta.list(list-->tuple'
    tupla=()
    for i in range(6):
        for j in range(10):
            if min(matriz[i][j]):
                tupla=(i,matriz[i][j])
    return tupla