def media_matriz (matriz):
    '''c'''
    vari=0
    vari2=0
    for i in matriz:
    	vari+= sum(i)
    	vari2+=len(i)
    return round(vari/vari2,2)