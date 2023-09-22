def conta_frases(texto):
    '''a funcao retorna o numero de frases do texto
str -> int'''
    exclamacao=str.count(texto, "!", 0, len(texto))
    interrogacao=str.count(texto, "?", 0, len(texto))
    ponto_final=str.count(texto, ".", 0, len(texto))
     
    return exclamacao+interrogacao+ponto_final