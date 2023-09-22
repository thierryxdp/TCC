def inverte(frase=''):
    '''função que dada uma frase retorna outra com as mesmas palavras,
    mas na ordem inversa, sem letras maiúsculas e sem a pontuação 
    string -> string''' 
frase.replace('.',' ').replace(';',' ').replace(',',' ').replace('-',' ').replace(':',' ').replace('?',' ').replace('!',' ')
frase = frase.split(' ')
return str(' ').join(frase[::-1])