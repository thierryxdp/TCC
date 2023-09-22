def conta_frases(frase):
    """Função que conta o número de frases que aparecem em um dado texto; str->int"""
    inte=str.count(frase,'?')
    ret=str.count(frase,'...')
    exc=str.count(frase,'!')
    pon=str.count(frase,'. ')
    ponf=str.count(frase,'.')
    return inte+ret+exc+pon+ponf