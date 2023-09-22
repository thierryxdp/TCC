def hashtag(s):
    """ Função que recebe uma string e insere o caractere # no
    início, meio e final da string.
    str-> str"""
    
    return '#' + s[:len(s)/2-1] + '#' + s[len(s)/2-1:] + '#'