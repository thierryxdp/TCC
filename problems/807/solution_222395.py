def conta_frases(x):
    """s"""
    x = str.replace(x,'...','.')
    x = str.count(x,'!')
    x = str.count(x,'?')
    x = str.count(x,'.')
    return (str.count(x,'!')+str.count(x,'?')+str.count(x,'.'))