def conta_frases(frases):
    """funcao que calcula o numero de frases que aparecem em um texto, sendo cada frase terminada com um ponto final, um ponto de exclamaca, ponto de interrogacao ou reticencias;
    str -> int"""
    saida=[]
    frases.replace('...','.')
    if '.' in frases:
        str.count(frases,'.')=saida[0]
    if '?' in frases:
        saida[0]+=str.count(frases,'?')
    if '!' in frases:
        saida[0]+=str.count(frases,'!')
    return int(saida[0])