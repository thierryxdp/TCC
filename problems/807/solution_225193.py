def conta_frases(frase):
    '''conta o numero de frases que aparecem numa string. Cada frase no texto e terminada com um ponto final,
um ponto de exclamacao, um ponto de interrogacao ou reticencias. str -> int'''
    exclamacao = frase.count("!")
    reticencias = frase.count("...")
    interrogacao = frase.count("?")
    nova = frase.replace("...","")
    final = nova.count(".")

    return exclamacao+reticencias+interrogacao+final