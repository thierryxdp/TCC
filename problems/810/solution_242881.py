def retira_pontuacao(frase):
    
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


        
def inverte(frase):
    
    ''' Função que retorna a frase de entrada
        com as palavras na ordem inversa, sem 
        letras maiúsculas e sem pontuação.
        str -> str '''
    
    frase = retira_pontuacao(frase)
    
    lista = frase.split()
    lista = lista.reverse()
    frase = ' '.join(lista)
    frase = frase.lower()
    
    return frase