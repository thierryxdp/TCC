def conta_frases(frase):
    '''Funcao que dado um texto armazenado em uma string, retorna o numero
    de frases que aparecem nesse texto
    str -> int'''
    ponto = (str.count(frase,'.'))
    exclamacao = (str.count(frase,'!'))
    interrogacao = (str.count(frase,'?'))
    reticencias = (str.count(frase,'...'))
    return ponto + exclamacao + interrogacao + reticencias