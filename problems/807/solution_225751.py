def conta_frases(frase):
    '''função que retorna o numero de frases inseridas'''
    '''str=>str'''
    ponto = frase.count(".")
    exclamacao = frase.count("!")
    interrogacao = frase.count("?")
    reticencias = frase.count("...")
    pontos = ponto+exclamacao+interrogacao+reticencias
    if reticencias >=1:
        return pontos - reticencias*3
        return pontos