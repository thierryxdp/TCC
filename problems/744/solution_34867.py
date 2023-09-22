def hashtag(s):
    ''' Recebe uma string e insere o caractere # no iniicio, no meio e no 
    final dela. Entrada. str -> str'''
    nova_string = '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'
    return nova_string