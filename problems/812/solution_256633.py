def retira_pontuacao(frase):
    '''funcao que dada uma frase, substitui suas pontuacoes por espacos
       string -> string'''
    str.replace(frase, '...', ' ')
    str.replace(frase, '.', ' ')
    str.replace(frase, '?', ' ')
    str.replace(frase, '!', ' ')
    str.replace(frase, '-', ' ')
    str.replace(frase, ',', ' ')
    str.replace(frase, ':', ' ')
    str.replace(frase, ';', ' ')
    return frase