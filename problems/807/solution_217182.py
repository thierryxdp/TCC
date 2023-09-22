def conta_frases(frase):
    '''Funcao que dado um texto armazenado em uma string, retorna o numero
    de frases que aparecem nesse texto
    str -> int'''
    ponto = (len(str.split(frase,'.')))-1
    exclamacao = (len(str.split(frase,'!')))-1
    interrogacao = (len(str.split(frase,'?')))-1
    reticencias = (len(str.split(frase,'...')))-4
    return ponto + exclamacao + interrogacao + reticencias