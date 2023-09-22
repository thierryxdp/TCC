def melhor_volta(matriz_tempos_volta):
    '''Fa ̧ca uma fun ̧c ̃ao chamada melhor volta que receba
    como entrada uma matriz 6 × 10 com os tempos
    em segundos dos corredores em cada volta. e retorna
    uma tupla para quem fez a menor volta quanto tempo foi
    e qual volta foi'''
    mini=0
    tupla = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz_tempos_volta[i][j] < tupla[1]:
                mini= min(matriz_tempos_volta[i][j])
                tupla = (i+1,mini,j+1)
            return tupla