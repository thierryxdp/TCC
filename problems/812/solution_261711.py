def retira_pontuacao (frase):
    '''Função que substitui as pontuações de uma frase por espaço.
    Usa-se str.replace() pra cada pontuação
    str >> str
    '''
    
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '...', ' ')
    
    return(frase)