def hashtag(s):
    '''retorna a string s com um hashtag no começo, no meio e no final;
    	string->string'''
    n=len(s)
    n2=len(s)//2
    if len(s)==1:
        return '#'+str(s)+'#'
    else:
        return '#'+str(s)[0:n2]+'#'+str(s)[n2:n]+'#'