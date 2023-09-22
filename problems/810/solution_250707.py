def remove(x):
    
    
    return str.lower(str.replace(str.replace(str.replace(str.replace(str.replace(x,',',' '),'...',' '),'.',' '),'?',' '),'!',' '))

def inverte(x):
    
    y = remove(x)
    
    w = str.split(y)
    
    list.reverse(w)
    
    return str.join(' ',w)