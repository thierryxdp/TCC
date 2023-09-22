def retira_pontuacao(frase):
    """ remove potuações das frases""" 
    pontuacoes = [ '--',
                  '...',
                   '.',
                  ';',
                  ':',
                  '?',
                  '!',
                  ',']
    return map(str.replace, pontuacoes,[frase]*len(pontuacoes),pontuacoes)