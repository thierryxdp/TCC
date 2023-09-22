def retira_pontuacao(s):
    '''Recebe uma frase e retorna esta mesma frase onde todos os caracteres 
    de pontuaçao forma substituidos por espaço;
    str -> str'''
    x=str.join(' ',(str.split(s,'...')))
    y=str.join(' ',(str.split(x,',')))
    z=str.join(' ',(str.split(y,':')))
    w=str.join(' ',(str.split(z,';')))
    e=str.join(' ',(str.split(w,'-')))
    r=str.join(' ',(str.split(e,'?')))
    t=str.join(' ',(str.split(r,'.')))
    q=str.join(' ',(str.split(t,'!')))
    
    return q