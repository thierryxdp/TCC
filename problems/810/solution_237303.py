def inverte(frase):
    '''Funcao que, dada uma frase, retorna a mesma na ordem inversa'''
    i = str.split(frase,' ')
    reverte = list.reverse(i)
    return str.join(' ',i)