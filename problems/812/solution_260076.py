def retira_pontuacao(frase):
    '''Entrada: frase (variável do tipo string)
       
       Saída: frase onde todos os caracteres de pontuação 
       tenham sido substituídod por espaço ( dado do tipo string)
       
       str -> str'''
    frase = frase.replace('.', ' ')
    frase = frase.replace('_', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace('!', ' ')
    frase = frase.replace('-', ' ')
    frase = frase.replace('?', ' ')
    return frase