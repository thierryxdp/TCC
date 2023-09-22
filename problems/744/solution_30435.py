def hashtag(s):
    '''funcao que insere o caracter # no inicio, no meio e no final da string s de entrada;
    str->str'''
    meio = math.ceil(len(s)/2)
    return '#' + s[0:meio] + '#' + s[meio:] + '#'