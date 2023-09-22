def hashtag(s):
    '''funcao hashtag que recebe um string e insere o caractere # o inicio, no meio e no final dela.
    string --> string'''
    media = len(s) // 2
    return "#" + s[0:media] + "#" + s[media:] + "#"