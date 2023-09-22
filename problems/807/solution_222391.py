def conta_frases(x):
    """s"""
    x = str.replase(x,'...','.')
    if '...' in x:
        return str.count(x,'...')
    elif '!' in x:
        return str.count(x,'!')
    elif '?' in x:
        return str.count(x,'?')
    elif '.' in x: 
        return str.count(x,'.')
    return (str.count(x,'...')+str.count(x,'!')+str.count(x,'?')+str.count(x,'.'))