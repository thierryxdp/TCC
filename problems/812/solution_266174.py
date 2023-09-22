def retira_pontuacao (frase):
    '''Função que retira a pontuação de uma frase
    string -> string'''
    simbolos_pontuacao = ['-', ',', ':', '.', ';']
    for c in simbolos_pontuacao:
        return frase.replace(c, ' ')