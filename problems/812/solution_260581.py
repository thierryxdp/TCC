def retira_pontuacao(frase):
    ''' retorna a frase sem pontuacao a partir 
    de um texto''''
    frase= str.replace(frase, '-', ' ')
    frase= str.replace(frase, ',', ' ')
    frase= str.replace(frase, ':', ' ')
    frase= str.replace(frase, ';', ' ')
    frase= str.replace(frase, '?', ' ')
    frase= str.replace(frase, '.', ' ')
    frase= str.replace(frase, '!', ' ')
    return frase