def conta_frases(frase):
    """função que conta o numero de frases str->str"""
    inte=str.count(frase,'?')
    etc=str.count(frase,'...')
    exc=str.count(frase,'!')
    pon=str.count(frase,'. ')
    ponf=str.count(frase,'.')
    if ponf==frase[-1]:
        return pon+exc+inte+etc+ponf
    
    else:
        return (pon+exc+inte+etc)