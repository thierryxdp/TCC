def media_matriz (matriz):
    '''c'''
    vari=0
    vari2=0
    for i in matriz:
        for j in i:
            vari+= matriz[i][j]
        	vari2+=j
    return round(vari/vari2,2)