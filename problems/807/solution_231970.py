def conta_frases(x):
    a=[]
    a=str.split(x,".")
    a=str.split(x,'!')
    a=str.split(x,'?')
    a=str.split(x,'...')
    return len(a)