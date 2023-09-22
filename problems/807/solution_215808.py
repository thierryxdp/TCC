def conta_frases(frase):
    """ função que receba e conte o número de frases que aparecem neste texto; str-> int"""
    r=0
    dot=0
    x=frase
    r= r+x.count('?')
    r= r+x.count('!')
    r = r+x.count('...')
    r = r+x.count('.')
    if(x.count('...')>0):
    	dot=x.count('...')
        r = r-(3*x.count('...'))
    return r