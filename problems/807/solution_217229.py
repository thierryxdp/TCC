def conta_frases(frase):
    '''Funcao que dado um texto armazenado em uma string, retorna o numero
    de frases que aparecem nesse texto
    str -> int'''
    reticencias = str.replace(frase,'...','.')
    reticencias = (str.count(reticencias,'...'))
    exclamacao = (str.count(frase,'!'))
    interrogacao = (str.count(frase,'?'))
    return exclamacao + interrogacao + reticencias