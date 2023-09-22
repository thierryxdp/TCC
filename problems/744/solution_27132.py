def hashtag (x):
    '''
        Função responsável por acrescentar hashtags no início, meio e final de uma string.
        x: String
        Saída: Str  => Str
    '''
    x = x
    s = len(x)//2
    return '#' + x[0:s] + '#' + x[s:] + '#'