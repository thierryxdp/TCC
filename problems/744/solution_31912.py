def hashtag(s):
    '''Recebe uma string e insere o caractere "#" no início,
    meio e fim dela.
    str -> str'''
    s = "#" + s[:len(str1)//2] + "#" + s[len(str1)//2:] + "#"
    return s