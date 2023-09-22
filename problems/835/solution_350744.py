def melhor_volta(matriz):
    'Dada uma matriz composta pelos tempos em segundos dos corredores em cada volta, retorne quem obteve a mehor prova e tambem com qual tempo e que volta.list(list-->tuple'
    tupla_melhor=()
    for i in range(6):
        for j in range(10):
            if matriz[i][j]<min(matriz):
                tupla_melhor=(i+1,matriz[i][j],j+1)
    return tupla_melhor