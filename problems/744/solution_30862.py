def hashtag(s):
    """ Função que recebe uma string e insere o caractere # no
    início, meio e final da string.
    str-> str"""
    
    return '#' + [:len(s)/2] + '#' + [len(s)/2:] + '#'