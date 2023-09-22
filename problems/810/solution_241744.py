def inverte(texto):
    '''Dado um texto, retorna a ordem das palavras invertida. str-->str'''	
    x=str.replace(texto,(','),' ')
    y=str.replace(x,(';'),' ')
    z=str.replace(y,('-'),' ')
    r=str.replace(z,('!'),' ')
    s=str.replace(r,(':'),' ')
    m=str.replace(s,('?'),' ')
    n=str.replace(m,('.'),' ')
    pontuacao= str.lower(n)
    o=str.split(pontuacao)[::-1]
    p=str.join(' ',o)
    return p