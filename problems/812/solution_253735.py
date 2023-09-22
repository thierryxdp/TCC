def retira_pontuacao(frase):
    '''dada uma frase, retorna a mesma porem com todos os caracteres de pontuação substituidos por espaço
    str -> str'''
    frase = str.replace (frase, '.', ' ')
    frase = str.replace (frase, ',', ' ')
    frase = str.replace (frase, '!', ' ')
    frase = str.replace (frase, '?', ' ')
    frase = str.replace (frase, ':', ' ')
    frase = str.replace (frase, '_', ' ')
    frase = str.replace (frase, ';', ' ')
    frase = str.replace (frase, '-', ' ')
    return frase