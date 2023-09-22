def retira_pontuacao (frase):
    '''Dada a frase a função retorna a propria frase mas trocando todos
       os caracteres de pontuação por espaço.
       str -> str'''
    frase = frase.replace('?', ' ')
    frase = frase.replace('!', ' ')
    frase = frase.replace('.', ' ')                    
    frase = frase.replace('-', ' ')
    frase = frase.replace(';', ' ')                     
    frase = frase.replace(':', ' ')                     
    frase = frase.replace(',', ' ')                     
    return frase