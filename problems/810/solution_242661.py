def retira_pontuacao(frase):
    '''
    Função que dada uma frase, retorna a mesma frase
    com remoção de todas as pontuações das frases.
    
    str->str
    '''
    frase= frase.replace('.',' ')
    frase=frase.replace('!',' ') 
    frase=frase.replace('?',' ')
    frase=frase.replace('-',' ') 
    frase= frase.replace(',',' ')
    frase= frase.replace(':',' ')
    frase= frase.replace(';',' ')
    return frase


def inverte(frase):
    '''
    Função que dada uma frase, retorna uma outra frase 
    com as mesmas palavras da frase de entrada na ordem 
    inversa e sem letras maiuscula, e sem a pontuação.
    
    str->str
    '''
    frase=retira_pontuacao
    frase.lower
    frase.sort(reverse=True)
    return frase