def upp(frase):
    ''' retorna a frase porém com todas as consoantes em maiúsculos.str-->str'''
    fraseNova=''
    contador=0
    while contador<len(frase):
        if frase[contador] in 'bcçdfghjklmnpqrstvwxyz':
            fraseNova= fraseNova + frase[contador].upper()
            contador=contador+1
        else:
            fraseNova= fraseNova + frase[contador]
            contador=contador+1
    return fraseNova