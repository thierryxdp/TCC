def retira_pontuacao(frase):
    '''Recebe uma frase e retorna a mesma frase sem nenhum dos caracteres de pontuação.
    string -> string'''

    s = frase
    a = str.replace(s, ',', ' ')
    b = str.replace(a, ':', ' ')
    c = str.replace(b, ';', ' ')
    d = str.replace(c, '.', ' ')
    e = str.replace(d, '...', ' ')
    f = str.replace(e, '!', ' ')
    g = str.replace(f, '?', ' ')
    final = str.replace(g, '    ', ' ')

    return final