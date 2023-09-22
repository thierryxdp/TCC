import math
def hashtag(s):
    '''
    str-> str'''
    
    y = list(s)
    z = ceil(len(s)/2)
    list.insert(y,0,'#')
    list.insert(y,z,'#')
    list.append(y,'#')
    x = ''.join(y)
    
    
    return x