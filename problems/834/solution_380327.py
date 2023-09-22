def media_matriz (matriz):
    '''c'''
    vari=0
    vari2=0
    rodada=1
    for i in matriz:
        for j in i:
            vari+=j
            vari2+=j+vari/j
        rodada+=1
    return vari2