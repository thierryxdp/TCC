def retira_pontuacao(texto):
    '''retira toda a pontuacao de uma frase dada, incluindo,vírgula,dois pontos,travessao
      str->str'''
      x = str.replace(texto, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a