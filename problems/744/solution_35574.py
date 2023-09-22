def hashtag(s):
    '''
    funcao retorna uma string com a substituicao e fatiamento
    str -> string
    '''
    a= s[0:len(s)//2]
    b= s[len(s)//2:len(s)]
    
    return '#' + a + '#' + b + '#'