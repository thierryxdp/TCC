def lingua_p(string):
    x=''
    for h in string:
        if h in 'aeiouAEIOU':
            x=x+h+'p'+ h
        else:
                x=x+ h
        
    return x