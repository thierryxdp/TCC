def conta_frases(frases):
    '''Funçao que dado um texto armazenado em uma string, retorna a funç̃ao
que conte o ńumero de frases que aparecem neste texto
str->int'''
    mud0=frases.replace('...','.')
    mud1=mud0.replace('?','.')
    mud2=mud1.replace('!','.')
    qntd=mud2.count('.')
    return qntd