def inverte (texto):
    '''função que retorna o inverso de uma frase dada, contendo
    as mesmas palavras da frase de entrada na ordem inversa'''
    b = str.lower(retira_pontuacao(texto))
    c = str.split(b)[::-1]
    d = str.join(' ',c)
    return d