def inverte(frase):
    '''Funcao que, dada uma frase, retorna a mesma na ordem inversa'''
    s = str.replace(frase,'.',' ').replace('!',' ').replace('?',' ').replace(',',' ')
    i = str.split(s,' ')
    inverte = list.reverse(i)
    return str.lower(str.join(' ',i))