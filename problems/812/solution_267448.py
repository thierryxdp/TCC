def retirapont(frase):
    '''função que recebe uma frase e troca todos os tipos de pontuação por espaços
str->str'''

    x=list(frase)
    
    if '-' in x:
        b=list.index(x,'-')
        x[b]=' '

    if '!' in x:
        c=list.index(x,'!')
        x[c]=' '

    if '?' in x:
        d=list.index(x,'?')
        x[d]=' '

    if ',' in x:
        e=list.index(x,',')
        x[e]=' '

    if ':' in x:
        f=list.index(x,':')
        x[f]=' '

    if ';' in x:
        g=list.index(x,';')
        x[g]=' '

    if '.' in x:
        h=list.index(x,'.')
        if x[h+1]!='.' and x[h-1]!='.':
            x[h]=' '
        if x[h+1]=='.' and x[h-1]=='.':
            x[h]=' '
            x[h+1]=''
            x[h-1]=''

    y=str.join('',x)

    return y