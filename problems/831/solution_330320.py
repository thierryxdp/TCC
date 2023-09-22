def lingua_p(string):
    x=''
    for h in string:
        if h in 'aeiouAEIOU':
            x=x+'p'+h+'p'
        else:
                x=x+ h
        
    return x