def retira_pontuacao(texto):
    '''Funcao que, dado um segmento de texto, retorna um outro em que todos os caracteres de pontuacao sao substituidos por espaco. Str -> str'''
    passo1 = str.replace(texto, ',', ' ')
    passo2 = str.replace(passo1, '-', ' ')
    passo3 = str.replace(passo2, ';', ' ')
    passo4 = str.replace(passo3, ':', ' ')
    passo5 = str.replace(passo4, '!', ' ')
    passo6 = str.replace(passo5, '?', ' ')
    passo7 = str.replace(passo6, '.', ' ')
    return passo7



def inverte(texto):
    final1 = retira_pontuacao(texto)
    final2 = str.lower(final1)
    separou = str.split(final2)
    virou = separou[::-1]
    completa = str.join(' ',virou)
    return completa