def lingua_p(p):
    '''função que recebe uma palavra em português
    e retorna-a para a lingua do p'''
    'str->str'
     if len(p)%2==0:
        pausa=len(p)//2
    else:
        pausa=(len(p)-1)//2
    return 'pa'+p[:pausa]+'pe'+p[pausa:]+'po'