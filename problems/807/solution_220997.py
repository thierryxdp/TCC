def conta_frases(frases):
    """funcao que calcula o numero de frases que aparecem em um texto, sendo cada frase terminada com um ponto final, um ponto de exclamaca, ponto de interrogacao ou reticencias;
    str -> int"""
    frases.replace('!','.')
    frases.replace('?','.')
    frases.replace('...','.')
    len(str.partition(frases,'.'))