def inverte(texto):
    ''' funçao que, fornecido um texto pelo usuario, 
    retorna o próprio, com as palavras invertidas
    str -> str
    '''
    b = str.lower(retira_pontuacao(texto))
    c = str.split(b)[::-1]
    d = str.join(' ',c)
    return d