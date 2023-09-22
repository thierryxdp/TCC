def conta_frases(x):
    """s"""
    x = str.replase(x,'...','.')
    x = str.count(x,'!')
    x = str.count(x,'?')
    x = str.count(x,'.')
    return (str.count(x,'!')+str.count(x,'?')+str.count(x,'.'))