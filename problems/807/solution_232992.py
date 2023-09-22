def conta_frases(frase):
    '''funcao que retornara o numero de frases inseridas.'''
    '''str=>str'''
    ponto=frase.count(".")
    exclamacao=frase.count("!")
    interrogacao=frase.count("?")
    reticencias=frase.count("...")
    pontos=ponto+exclamacao+recicencias+interrogacao
if reticencias>=1:
    return pontos-reticencias*3