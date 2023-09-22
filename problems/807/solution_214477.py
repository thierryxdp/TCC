def conta_frases (texto):
    """"funcao que conta as frases de um texto, sendo o termino da frase determinado por: ponto final, ponto de exclamacao, ponto de interrogacao e reticencias
    str -> int"""
    return str.count("(texto)","!")+str.count("(texto)","?")+str.count("(texto)",".")+str.count("(texto)","...")