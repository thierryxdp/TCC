def hashtag(s):
    '''Essa função recebe como entrada uma string, e retorna 
    uma string com o caractere '#' entre a string dada
    str->str'''
    meio=len(s)//2
    return '#'+ s[:meio]+'#'+s[meio:]+'#'