def verificaCaracter(c):
    pontuacoes =[
        '--',
        '...',
        '.',
        ';',
        '!',
        '?',
        ',',
        ':'
    ]
    return '' if c in pontuacoes else c
def retira_pontuacao(frase):
    """ Remover todas as Pontuacoes da frase """
    fraseAlterada=str.join('',list(map(verificaCaracter, frase)))
    return fraseAlterada