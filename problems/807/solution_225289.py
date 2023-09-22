def conta_frases(texto):
    """Função que conta o número de frases que aparecem em um dado texto; str->int"""
    inte=str.count(frase,'?')
    etc=str.count(frase,'...')
    exc=str.count(frase,'!')
    pon=str.count(frase,'. ')
    ponf=str.count(frase,'.')
    if ponf==frase[-1]:
        return pon+exc+inte+etc+ponf
    
    else:
        return (pon+exc+inte+etc)