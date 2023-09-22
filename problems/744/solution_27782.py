def hashtag(s):
    """Esta função recebe uma string e insere o caractere "#" no inicio, no meio e fim dessa frase."""
    return '#' + s[0:len(s)//2] + '#' + s[len(s)//2:] + '#'