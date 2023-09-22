def hashtag(s):
    '''Recebe uma string e insere o caractere "#" no início,
    meio e fim dela.
    str -> str'''
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s