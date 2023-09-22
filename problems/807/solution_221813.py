def conta_frases(texto):
    '''Funcao recebe um texto e retorna a quantidade de frases que exitem nele, tendo como como termino de frases ", . ; !" etc
string -> int'''
    reticencias =(str.count(texto.strip(), '...'))
    ponto = (str.count(texto.strip(), '.')) - (reticencias * 3)
    doipontos = (str.count(texto.strip(), ':'))
    esclamacao = (str.count(texto.strip(), '!'))
    interrogacao = (str.count(texto.strip(), '...'))
    if (ponto>0):
        return reticencias + ponto + esclamacao + interrogacao + doipontos
    else:
        return reticencias + doipontos + esclamacao + interrogacao