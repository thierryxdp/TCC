def retira_pontuacao():
    """ remove potuações das frases""" 
    pontuacoes = [ '--',
                  '...',
                   '.',
                  ';',
                  ':',
                  '?',
                  '!',
                  ',']
    return map(str.frase.replace, pontuacoes,[' ']*len(pontuacoes))