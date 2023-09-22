def inverte(frase):
    '''Função que dada uma frase de entrada retorna outra frase com as 
    palavras na ordem inversa, sem letras maiúsculas e sem pontuação 
    str -> str'''
    frase = frase.lower()
    frase = frase.replace(',',' ').replace('.','').replace('-',' ').replace(';','').replace(':','').replace('?','').replace('!','').replace('...','')
    frase = frase.split()
    frase.reverse()
    frase = str.join(' ', frase)
    return frase