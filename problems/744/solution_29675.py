import math
def hashtag(s):
    '''
    str-> str'''
    
    y = list(s)
    z = math.ceil(len(s)/2)
    list.insert(y,0,'#')
    list.insert(y,z,'#')
    list.append(y,'#')
    x = ''.join(y)
    
    t = math.ceil(len(s)/2)+1
    list.insert(y,0,'#')
    list.insert(y,z,'#')
    list.append(y,'#')
    x = ''.join(y)
    
    
    if (len(s)%2)==0:
        y = list(s)
        z = math.ceil(len(s)/2)
        list.insert(y,0,'#')
        list.insert(y,z,'#')
        list.append(y,'#')
        x = ''.join(y)
        return x
    else:
        y = list(s)
        z = math.ceil(len(s)/2)+1
        list.insert(y,0,'#')
        list.insert(y,z,'#')
        list.append(y,'#')
        x = ''.join(y)
        return x