def conta_frases(frases):
    ''' função que conta quantas frases tem num texto
    str-> int'''
    #esse código é uma versão emprensada onde procura cada termino possivel individualmente para depois contar
    return len(str.split(str.replace(str.replace(str.replace(str.replace(frases,'!',' '),'?',' '),'.',' '),'...',' ')))