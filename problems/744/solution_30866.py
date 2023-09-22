def hashtag(s):
    """ Função que recebe uma string e insere o caractere # no
    início, meio e final da string.
    str-> str"""
    
    x=str(s)
    y= len(x)/2-1
    
    return '#' + s[:y]+'#' + s[y:]+'#'