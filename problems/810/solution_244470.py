def inverte(frase):
    '''Funcao que dada uma frase, retorna outra frase que contenha as mesmas palavras na ordem 
    inversa, sem letras maiúsculas, e sem pontuacao 
    str-> str
    '''
    #remover pontuacao
    frase=frase.replace('-',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('...',' ')
    frase=frase.replace('.',' ')
	#remover letras maiusculas
    frase=frase.lower()
    #frase inversa
    return frase.reverse()