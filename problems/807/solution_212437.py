def conta_frases(a):
    if '.' in a:
       a=str.split(a,'.')
    elif '?' in a:
       a=str.split(a,'?')
    elif '!' in a:
       a=str.split(a,'!')
     str.strip(str(a))
        return len(a)