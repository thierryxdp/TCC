def conta_frases(x):
    x = str.replace(x,'...','*')
    x =str.replace(x,'.','*')
    x =str.replace(x,'!','*')
    x =str.replace(x,'?','*')
    y = len(str.split(x,*))
    return y