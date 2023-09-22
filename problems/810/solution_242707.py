def retira_pontuacao(frase):
    '''Função que retira a pontuação de um dada frase
    str -> str'''
    a = str.replace(frase, '-', ' ')
    b = str.replace(a, ',', '')
    c = str.replace(b, ':', '')
    d = str.replace(c, ';', '')
    e = str.replace(d, '...', '')
    f = str.replace(e, '.', '')
    g = str.replace(f, '!', '')
    h = str.replace(g, '?', '')
    return h
def inverte(frase):
    '''Função que retira a pontuação, deixa em minúsculo e inverte a ordem das palavras de uma 
    dada frase
    str -> str'''
    sem_pontuacao = retira_pontuacao(frase)
    minusculo = str.lower(sem_pontuacao)
    lista = str.split(minusculo)
    list.reverse(lista)
    frase_invertida = str.join(' ', lista)
    return frase_invertida