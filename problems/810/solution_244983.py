def inverte(frase):
    '''
       Função que recebe uma frase e retira todas as suas pontuações
       e inverte de trás para frente as palavras
       str --> str
    '''
    
    frase = frase.replace(',','')
    frase = frase.replace('-','')
    frase = frase.replace(':','')
    frase = frase.replace(';','')
    frase = frase.replace('.','')
    frase = frase.replace('?','')
    frase = frase.replace('!','')
    splitar = frase.split()
    splitar.reverse()
    
    return ' '.join(splitar)