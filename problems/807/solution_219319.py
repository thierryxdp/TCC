def conta_frases(frase):
    """essa função recebe um texto e conta quantas frases esse possui, analisando através das pontuações finais de cada frase
    str-> int"""
    x=str.replace(str.replace(str.replace(str.replace(frase,'...', '#'),'.', '#'),'!', '#'),'?', '#')
    return str.count(x,'#')