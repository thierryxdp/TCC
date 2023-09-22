def retira_pontuacao(texto):
    ''' Essa função troca todos os caracteres de pontuação por espaço.'''
    ''' Entrada = string ; saída = string '''
    pontuacao = '.,:;-'
    frase = str.replace(texto,pontuacao,' ')
    return frase