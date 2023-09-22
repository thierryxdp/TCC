def hashtag(s):
    '''Função que recebe uma string e insere o '#' no início,
no meio e no final dela;
    str-> str'''
    if(len(s)%2==0):
        s1=s[0:len(s)+1:3]+'#'
        return '#'+s1
    else:
        s2=s[0:len(s)-2:3]+'#'
        return '#'+s2+'#'