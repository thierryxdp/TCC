def conta_frases(x):
    """s"""
    ...= frase.count('...')
    . = frase.count('.')
    . = .-...*3
    if '...' in x:
        return str.count(x,'...')
    elif '!' in x:
        return str.count(x,'!')
    elif '?' in x:
        return str.count(x,'?')
    elif '.' in x: 
        return str.count(x,'.')
    return (str.count(x,'...')+str.count(x,'!')+str.count(x,'?')+str.count(x,'.'))