def conta_frases(texto):
    '''Função que retona a quantidade de frases dentro de uma string
    
    	str -> int'''
    x=texto.replace('...','?')
    y=x.replace('.','?')
    z=y.replace('!','?')
    return str.count(z,'?')