def inverte(frase): 
    '''função que dada uma frase retorna
    uma outra com as mesmas palavras,
    mas na ordem inversa, sem letras maiúsculas
    e sem a pontuação string -> string'''
frase1 = frase.replace('.',' ').replace(';',' ').replace(',',' ').replace('-',' ').replace(':',' ').replace('?',' ').replace('!',' ')
frase2 = frase1.lower
frase3 = frase2.reverse
frase_nova = frase3[::-1]