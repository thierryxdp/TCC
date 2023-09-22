def conta_frases(frase):
    '''uma funcao que conta o numero de frases'''
pont=frase.count(".")
exclamacao=frase.count("!")
interrogacao=frase.count("?")
reticencias=frase.count("...")
pontos=pont+exclamacao+reticencias+interrogacao
if reticencias >= 1:
return pontos - reticencias*3
return ponto