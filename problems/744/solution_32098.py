def hashtag(s):
    '''Recebe uma string e insira o caractere "#" no início, no meio
    e no final dela.
    str -> str'''
    tam = len(s)
    #Mesmo raciocínio da questão anterior
    return '#' + s[:tam//2] + '#' + s[tam//2:] + '#'