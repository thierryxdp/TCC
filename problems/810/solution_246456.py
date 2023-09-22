def retira_pontuacao(texto):
    '''Função que, fornecido um texto pelo usuario, retorna o mesmo,
    porem sem nenhuma pontuação, substituindo por espaços;
    str -> str'''

    x = str.replace(texto, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a

def inverte(texto):
    '''Função que, fonecido um texto pelo usuario, retorna o próprio, 
    com a ordem das palavras invertida
    str -> str
    '''
    b = str.lower(retira_pontuacao(texto))
    c = str.split(b)[::-1]
    d = str.join(' ',c)
    return d