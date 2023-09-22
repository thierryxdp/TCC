def conta_frases(x):
    str.replace(x,'...','*')
    str.replace(x,'.','*')
    str.replace(x,'!','*')
    str.replace(x,'?','*')
    return len(str.split(x,*))