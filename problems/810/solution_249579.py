def inverte(frase):
    '''Função que dada uma frase retorna uma outra frase que contam as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas e pontuação
       str->str'''
	frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.lower(frase)
    frase.reverse()
    frase = str.join(' ',frase)
    return frase