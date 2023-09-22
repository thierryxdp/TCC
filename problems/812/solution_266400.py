def retira_pontuacao(fr):
    '''Dada uma frase, retorna a frase onde todos os caracteres de pontuação (incluindo
    travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase)
    tenham sido substituídos por espaço.
    str --> str'''
    if fr == '':
        return fr
    frase = []
    frase[:] = fr
    n = x = len(frase)
    while n>0 :
        n = n-1
        if frase[n] == ',':
            frase[n] = ' '
        if frase[n] == '.':
            frase[n] = ' '
        if frase[n] == ':':
            frase[n] = ' '
        if frase[n] == ';':
            frase[n] = ' '
        if frase[n] == '-':
            frase[n] = ' '
        if frase[n] == '?':
            frase[n] = ' '
        if frase[n] == '!':
            frase[n] = ' '

    while x>1:
        frase[-1] = frase[-2] + frase[-1]
        del(frase[-2])
        x = x-1

    return frase[0]