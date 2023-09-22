def hashtag(s):
    '''Função que recebe uma string e retorna essa mesma string
    com a adição de # no início, meio e fim da string
    str-> str'''
    metade= len(s)//2
    return '#' + s[0:metade] + '#' +s[metade+1:]+ '#'