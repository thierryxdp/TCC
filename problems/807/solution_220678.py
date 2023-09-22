def conta_frases(frase:str)->int:
    '''Funcao que retorna numero de frases que aparecem no texto'''
    x=str.index(frase,'?')
    y=str.index(frase,'!')
    return str.count(frase,'.',0,y)+str.count(frase,'!',0)+str.count(frase,'?',0)+str.count(frase,'.',-2,x)