def conta_frases(x):
    x = str.replace(x,'...','*')
    x =str.replace(x,'.','*')
    x =str.replace(x,'!','*')
    x =str.replace(x,'?','*')
    x = len(str.split(x,*))
    return x