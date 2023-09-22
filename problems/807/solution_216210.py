def conta_frases(x):
    '''comentario
    str->int'''
    ponto==(len(str.split(x,'.')))-1
    exclamacao==(len(str.split(x,'!')))-1
    interrogacao==(len(str.split(x,'?')))-1
    reticencias==(len(str.split(x,'...')))-1
    return ponto+exclamacao+interrogacao+reticecias