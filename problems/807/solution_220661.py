def conta_frases(frase:str)->int:
    '''Funcao que retorna numero de frases que aparecem no texto'''
    x=str.find(frase,'!')
    y=str.find(frase,'?')
    z=str.find(frase,'?')+2
    return str.count(frase,'.',0,x)+str.count(frase,'!',0)+str.count(frase,'?',0)+str.count(frase,'.',y,z)