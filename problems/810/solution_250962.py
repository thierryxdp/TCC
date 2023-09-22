def inverte(frase): 
    '''função que dada uma frase retorna
    uma outra com as mesmas palavras,
    mas na ordem inversa, sem letras maiúsculas
    e sem a pontuação string -> string'''
frase = ""
a = frase.replace('.',' ').replace(';',' ').replace(',',' ').replace('-',' ').replace(':',' ').replace('?',' ').replace('!',' ')
b = frase.lower
c = frase.reverse
frase_nova = "a+b+c"