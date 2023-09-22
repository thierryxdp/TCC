def conta_frases(texto):
    """funcao que calcula quantas frases tem um texto, 
    de acordo com quantos pontos finais, ponto de 
    interrogacao, ponto de exclamacao e reticencias 
    aparecem, e retorna quantas frases tem no texto.
    str->int"""
    x = str.count(texto,".")
    y = str.count(texto,"?")
    z = str.count(texto,"!")
    w = str.count(texto,"...")

    return (x-(3*w))+y+z+w