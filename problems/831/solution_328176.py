def lingua_p(p):
    ''' Função que converte palavras em português p em palavras da lingua do P.'''
    d=list(p)
    f=''
    j=0
    for i in d:
        f=f+i
        if ( (i=='a') or (i=='e') or (i=='i') or (i=='o') or (i=='u')):
            f=f+'p'+i
     
    return f