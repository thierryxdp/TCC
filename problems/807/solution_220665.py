def conta_frases(frase:str)->int:
    '''Funcao que retorna numero de frases que aparecem no texto'''
    x=str.find(frase,'!')
    y=str.find(frase,'.')+1
    return str.count(frase,'.',0,y)+str.count(frase,'!',0)+str.count(frase,'?',0)+str.count(frase,'.',x,-2)