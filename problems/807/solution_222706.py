def conta_frases(texto):
    '''Funcao recebe um texto e retorna a quantidade de frases que exitem nele, tendo como como termino de frases ", . ; !" etc
string -> int'''
    texto = str.join("ppjj", str.split(texto, '...'))
    reticencias =(str.count(texto.strip(), 'ppjj'))
    ponto = (str.count(texto.strip(), '.'))
    esclamacao = (str.count(texto.strip(), '!'))
    interrogacao = (str.count(texto.strip(), '?'))
    return reticencias + ponto + esclamacao + interrogacao