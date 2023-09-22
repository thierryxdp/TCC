def inverte(frase):
    '''
    Função que dada uma frase, retorna uma outra frase 
    com as mesmas palavras da frase de entrada na ordem 
    inversa e sem letras maiuscula, e sem a pontuação.
    
    str->str
    '''
    frase1=retira_pontuacao(frase)
    frase1.lower
    frase1.reverse
    return frase1