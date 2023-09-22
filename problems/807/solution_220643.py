def conta_frases(frase:str)->int:
    '''Funcao que retorna numero de frases que aparecem no texto'''
    return str.count(frase,'.',0)+str.count(frase,'!',0)+str.count(frase,'?',0)+str.count(frase,'...',0)