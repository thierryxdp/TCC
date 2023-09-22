def hashtag(s):
    '''função que retorna uma string com um '#' no começo, no meio e no fim
    da string;
    string->string'''
    a = len(s)
    b = int((len(s))//2)
    s_resultante1 = '##'+s[0:a]+'#'
    s_resultante2 = '#'+s[0:b]+'#'+s[b::]+'#'
    
    if len(s)==1:
        return s_resultante1 
    else:
        return s_resultante2