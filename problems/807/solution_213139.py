def conta_frases(frase):
    """calculo e retorno da funcao que conta o numero de frases que aparecem no texto"""
    x=frase
    b= len(x.split('!','?','.'))
    d= x.count('...')
    return b-d