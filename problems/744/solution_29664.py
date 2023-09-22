def hashtag(s):
    '''
    str-> str'''
    
    y = list(s)
    z = round(len(s))
    list.insert(y,0,'#')
    list.insert(y,z,'#')
    list.append(y,'#')
    x = ''.join(y)
    
    
    return x