def lingua_p(string):
    x=''
    for h in string:
        if h in 'aeiouAEIOUúáéíó':
            x=x+h+'p'+ h
        else:
                x=x+ h
        
    return x