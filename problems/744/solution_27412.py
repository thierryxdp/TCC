def hashtag(s):
    '''Funcao que insere o caractere '#' no inicio, meio e no final de uma string;
    str -> str'''
    meio = len(s)//2
    return '#' + s[:meio] + '#' + s[meio:] + '#'