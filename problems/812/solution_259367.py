def verificaCaracter(c):
     pontuacoes = [ '--',
                  '...',
                   '.',
                  ';',
                  ':',
                  '?',
                  '!',
                  ',']

    return '' if c in pontuacoes c




def retira_pontuacao(frase):
    """ remove potuações das frases""" 
    fraseAlterada =str.join(
        '',
        map(verificaCaracter, frase)
    )
    return fraseAlterada