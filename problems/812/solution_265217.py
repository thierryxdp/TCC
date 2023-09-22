def retira_pontuacao(texto):
    ''' Essa função troca todos os caracteres de pontuação por espaço.'''
    ''' Entrada = string ; saída = string '''
    pontuacao = '.'
    pontuacao1= ','
    pontuacao2= ';'
    pontuacao3=':'
    pontuacao4='-'
    frase = str.replace(texto,pontuacao,' ')
    frase1 = str.replace(texto,pontuacao1,' ')
    frase2 = str.replace(texto,pontuacao2,' ')
    frase3 = str.replace(texto,pontuacao3,' ')
    frase4 = str.replace(texto,pontuacao4,' ')
    return frase4