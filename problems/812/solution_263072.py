def retira_pontuacao(texto):
    '''Função, fornecida um texto pelo usuario, retorna o mesmo,
   porém sem nenhuma pontuação, substituindo todas por espaços;
   str -> str'''

    x = str.replace(texto, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a