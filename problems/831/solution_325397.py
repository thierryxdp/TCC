def lingua_p(palavra):
    s = ''
    x=0
    while x<len(palavra):
        if palavra[x] in 'aeiou':
            s=s+palavra[x+1].index('p')
            s=s+palavra[x-1].index('p')
            
        else: 
            s=s+palavra[x]
        x=x+1
    return s