def conta_frases(x):
    '''comentario
    str->int'''
    ponto is(len(str.split(x,'.')))-1
    exclamacao is(len(str.split(x,'!')))-1
    interrogacao is(len(str.split(x,'?')))-1
    reticencias is(len(str.split(x,'...')))-1
    return ponto+exclamacao+interrogacao+reticecias