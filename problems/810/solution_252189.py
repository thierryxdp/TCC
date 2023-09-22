def retira_pontuacao(frase):
    '''Dada uma frase, retorna a frase onde todos os caracteres de pontuação (incluindo
    travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase)
    tenham sido substituídos por espaço.
    str --> str'''
    if frase == '':
        return frase

    frase = str.replace(frase, '.', ' ',)
    frase = str.replace(frase, ',', ' ',)
    frase = str.replace(frase, '-', ' ',)
    frase = str.replace(frase, ':', ' ',)
    frase = str.replace(frase, ';', ' ',)
    frase = str.replace(frase, '?', ' ',)
    frase = str.replace(frase, '!', ' ',)

    return frase




#4


def inverte(texto):
    '''Dada uma frase retorna uma outra frase que contenha as mesmas palavras da frase
    de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.'''

    texto = str.lower(texto)
    
    texto = retira_pontuacao(texto)
 
    
    frase = str.split(texto)

    
    list.reverse(frase)

    return str.join(' ',frase)