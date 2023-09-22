def inverte(x=""): 
    '''função que dada uma frase retorna
    uma outra com as mesmas palavras,
    mas na ordem inversa, sem letras maiúsculas
    e sem a pontuação string -> string'''
   x= x.replace('.',' ').replace(';',' ').replace(',',' ').replace('-',' ').replace(':',' ').replace('?',' ').replace('!',' ')
   x= x.split(" ")
   return str(" ").join(x[::-1])