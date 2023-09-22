def hashtag(s):
    '''Dado uma string, retorna a mesma com 3 #, 
    cada uma no comeco, meio e fim.
    str-> str'''
    c = len(s)//2
    m = s[c]
    
    return ("# + s[0:m]+ # +[m::]+ #")