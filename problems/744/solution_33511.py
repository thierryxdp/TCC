def hashtag(s):
    '''
    função que recebe uma string e insira o caractere # no inicio, 
    meio e fim da mesma
    str-> str
    '''
    x= len(s)//2
    s = '#' + s[0:x] + '#' + s[x:] + '#'
    return s