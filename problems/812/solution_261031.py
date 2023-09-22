retira_pontuacao(frase):
    
    ''' Função que retorna frase dada sem
        seus caracteres de pontuação.
        str -> str '''
    
    
    frase = frase.replace('...','/')
    frase = frase.replace('.','/')
    frase = frase.replace('!','/')
    frase = frase.replace('?','/')
    frase = frase.replace('.','/')
    frase = frase.replace('-','/')
    frase = frase.replace(',','/')
    frase = frase.replace(';','/')
    
    frase = frase.replace('/', ' ')
    
    return frase