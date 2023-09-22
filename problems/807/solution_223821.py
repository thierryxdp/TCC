def conta_frases(frase):
    """ retorna o numero de frasesterminando com um ponto final, exclamacao, interrogacao ou
    reticencias.
    str->str"""
    ponto = str.count(frase,'.',0)
    exclamacao = str.count(frase,'!',0)
    interrogacao = str.count(frase, '?', 0)
    reticencias = str.count(frase, '...',0)
    return ponto + exclamacao + interrogacao + -2* reticencias