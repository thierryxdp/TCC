def hashtag(s):
    '''
    str-> str'''
    
    y = list(s)
    z = round(len(s))
    list.insert(y,0,'#')
    list.insert(y,z,'#')
    list.insert(y,-1,'#')
    
    return y