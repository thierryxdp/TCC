def melhor_volta(matriz_tempos_volta):
    '''Fa ̧ca uma fun ̧c ̃ao chamada melhor volta que receba
    como entrada uma matriz 6 × 10 com os tempos
    em segundos dos corredores em cada volta. e retorna
    uma tupla para quem fez a menor volta quanto tempo foi
    e qual volta foi'''
    tupla = (0,0.0,0)
    for i in range(6):
        for j in range(10):
            if matriz_tempos_volta[i][j] > tupla[i]:
                 tupla = (i+1,matriz_tempos_volta[i][j],j+1)
            return tupla