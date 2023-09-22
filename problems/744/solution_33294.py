def hashtag(s):
    '''Função que recebe uma string e insere o '#' no início,
no meio e no final dela;
    str-> str'''
    if((len(s)%2)!=0):
        s1=s[0:(len(s)+1)/2]+'#'
        s2=s[((len(s)+1)/2)-1:-1]+'#'
        return '#'+str(s1)+str(s2)