def conta_frases(frase):
    '''Função que conta quantas frases existem
    num dado texto, lembrando que cada frase é
    tida como até um ponto final (.), um ponto
    de exclamação (!), um ponto de interrogação
    (?) ou reticências (...)
    str -> int'''
    final = str.split(frase,".")
    excl = str.split(frase,"!")
    inter = str.split(frase,"?")
    reti = str.split(frase,"...")
    resultado = len(final)+len(excl)+len(inter)+len(reti)
    return resultado