def retira_pontuacao(fr):
    '''Dada uma frase, retorna a frase onde todos os caracteres de pontuação (incluindo
    travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase)
    tenham sido substituídos por espaço.
    str --> str'''
    if fr == '':
        return fr

    frase = str.replace(frase, '.', ' ',)
    frase = str.replace(frase, ',', ' ',)
    frase = str.replace(frase, '-', ' ',)
    frase = str.replace(frase, ':', ' ',)
    frase = str.replace(frase, ';', ' ',)
    frase = str.replace(frase, '?', ' ',)
    frase = str.replace(frase, '!', ' ',)

    return frase