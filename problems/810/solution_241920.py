def inverte(texto):
    '''retorna um texto invertido a partir do termo "texto"'''
      b = str.lower(retira_pontuacao(texto))
    c = str.split(b)[::-1]
    d = str.join(' ',c)
    return d