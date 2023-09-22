def conta_frases(x):
    """s"""
    if '.' in x:
        return str.count(x,'.')
    if '!' in x:
        return str.count(x,'!')
    if '?' in x:
        return str.count(x,'?')
    if '...' in x:
        return str.count(x,'...')
    return (str.count(x,'.')+str.count(x,'!')+str.count(x,'?')+str.count(x,'...'))