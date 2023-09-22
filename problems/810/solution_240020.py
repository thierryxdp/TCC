def inverte(s):
    '''Recebe uma frase e retorna essa frase na ordem inversa, sem letras
    maiusculas e sem a pontuaçao;
    str -> str'''
    x=str.join(' ',(str.split(s,'...')))
    y=str.join('',(str.split(x,',')))
    q=str.join(' ',(str.split(y,'-')))
    w=str.join(' ',(str.split(q,';')))
    e=str.join(' ',(str.split(w,'!')))
    r=str.join(' ',(str.split(e,'?')))
    t=str.join(' ',(str.split(r,'.')))
    u=str.split(t)
    i=u[::-1]
    return str.join(' ',i)