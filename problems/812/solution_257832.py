def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna a frase onde todos os caracteres de pontuação foram substituidos por espaços em branco.
    string -> string'''
    p = str.replace(frase, ',', ' ')
    p2 = str.replace(p, '.', ' ')
    p3 = str.replace(p2, '?', ' ')
    p4 = str.replace(p3, '!', ' ')
    p5 = str.replace(p4, ':', ' ')
    p6 = str.replace(p5, '-', ' ')
    p7 = str.replace(p6, ';', ' ')
    return p7