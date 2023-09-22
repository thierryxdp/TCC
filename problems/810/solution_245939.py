def inverte(frase):
    '''Função que dada uma frase retorna uma outra frase que contém as mesma palavras da original na ordem inversa, sem letras maiúsculas e sem a pontuação: string -> string'''
    frase = frase.lower(frase)
    frase = frase.replace(frase,',',' ').replace('.','').replace('-','').replace(';','').replace(':','').replace('?','').replace('!','').replace('...','')
    frase = frase.split()
    frase = frase.reverse()
    return frase