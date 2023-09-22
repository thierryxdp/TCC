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
def inverte (frase):
    ''' Entrada: frase (variável do tipo string)
    	
        Saída: frase2 (variável do tipo string que contem as mesmas 
        palavras da frase de entrada na ordem inversa
        
        str -> str'''
    frase = frase.lower()
    frase = frase.split(' ')
    frase = frase[::-1]
    frase = ' '.join(frase)
    return frase