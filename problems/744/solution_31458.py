def hashtag (s):
    '''Função que recebe uma string e insire o caractere ”#” no início,
no meio e no final dela.'''
    #string -> string
    #funcina com números
    s = str(s)
    return '#' + s[:len(s) // 2] + '#' + s[len(s) // 2:] + '#'