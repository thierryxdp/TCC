def hashtag(s):
    """ Função que recebe uma string e insere o caractere # no
    início, meio e final da string.
    str-> str"""
    x=len(s)/2-1
    
    return '#' + s[:x] +'#' + s[x:]+'#'