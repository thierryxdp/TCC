def conta_frases(frase):
    '''uma funcão que conta o numero de frases'''
ponto=frase.count(".")
exclamacao=frase.count("!")
interrogacao=frase.count("?")
reticencias=frase.count("...")
pontos=ponto+exclamacao+reticencias+interrogacao
if reticencias > = 1:
    return pontos - reticencias*3