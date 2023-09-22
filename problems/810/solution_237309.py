def inverte(frase):
    '''Funcao que, dada uma frase, retorna a mesma na ordem inversa'''
    i = str.split(frase,' ')
    inverte = list.reverse(i)
    p = str.replace(i,'.',' ').replace('!',' ').replace('?',' ')
    return str.lower(str.join(' ',i))