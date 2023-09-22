def conta_frases(frase):
    '''Funcao que dado um texto armazenado em uma string, retorna o numero
    de frases que aparecem nesse texto
    str -> int'''
    ret = str.replace(frase,'...','.')
    reticencias = (str.count(frase,ret))
    exclamacao = (str.count(frase,'!'))
    interrogacao = (str.count(frase,'?'))
    return exclamacao + interrogacao + reticencias