def hashtag(string):
    '''Recebe uma string e insira o caractere "#" no início, no meio
    e no final dela.
    str -> str'''
    tam = len(string)
    #Mesmo raciocínio da questão anterior
    return '#' + string[:tam//2] + '#' + string[tam//2:] + '#'