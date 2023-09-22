def retira_pontuacao(frase):
    '''Funcao que dada uma frase, retorna todos caracteres de pontuacao substituidos por espaco
    str-> str
    '''
    frase=frase.replace('-',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('...',' ')
    frase=frase.replace('.',' ')
    return frase

def inverte(frase):
    '''Funcao que dada uma frase, retorna outra frase que contenha as mesmas palavras na ordem 
    inversa, sem letras maiúsculas, e sem pontuacao 
    str-> str
    '''
    #remover pontuacao
    frase=retira_pontuacao(frase)
    #remover letras maiusculas
    frase=frase.lower()
    #frase inversa
    frase=frase.split()
    frase=frase[::-1]
    frase.join()
    return frase.join()