def inverte(frase):
    '''Função que dada uma frase retorna uma outra frase que contém as mesma palavras da original na ordem inversa, sem letras maiúsculas e sem a pontuação: string -> string'''
    frase = str.lower(frase)
    frase = str.replace(frase,',',' ').replace('.','').replace('-','').replace(';','').replace(':','').replace('?','').replace('!','').replace('...','')
    frase = str.split(frase)
    frase = str.join(' ',(frase.reverse))
    return frase