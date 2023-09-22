def hashtag(string):
    '''Funcao que recebe uma string e retorna
    a string com o caractere '#' no inicio, meio
    e fim dela.
    EX: 'hashtag' -> '#has#htag#'.'''
    from math import floor
    indice_metade=floor(len(string)/2)
    metade1=string[:indice_metade]
    metade2=string[indice_metade:]

    return '#'+ metade1+'#'+metade2+'#'