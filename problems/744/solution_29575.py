def hashtag(s):
    '''
       Função que recebe uma string (s) e retorna a mesma
       string, porem com tres # inseridas: uma no começo, uma
       no final e uma no meio de s;
       str-> str
    '''
    has = '#'+s[0:len(s)//2]+'#'+s[len(s)//2:]+'#'
    return has