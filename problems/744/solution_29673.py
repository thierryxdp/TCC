import math
def hashtag(s):
    '''
    str-> str'''
    
    y = list(s)
    z = math.ceil(len(s)/2)+1
    list.insert(y,0,'#')
    list.insert(y,z,'#')
    list.append(y,'#')
    x = ''.join(y)
    
    
    return x