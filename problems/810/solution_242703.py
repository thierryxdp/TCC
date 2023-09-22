def retira_pontuacao(frase):
    '''Função que retira a pontuação de um dada frase
    str -> str'''
    a = str.replace(frase, '-', '')
    b = str.replace(a, ',', '')
    c = str.replace(b, ':', '')
    d = str.replace(c, ';', '')
    e = str.replace(d, '...', '')
    f = str.replace(e, '.', '')
    g = str.replace(f, '!', '')
    h = str.replace(g, '?', '')
    return h
def inverte(frase):
    sem_pontuacao = retira_pontuacao(frase)
    minusculo = str.lower(sem_pontuacao)
    lista = str.split(minusculo)
    lista_invertida = list.reverse(lista)
    frase_invertida = str.join(' ', lista_invertida)
    return frase_invertida