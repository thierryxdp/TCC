def lingua_p(palavra):
    s = ''
    x=0
    while x<len(palavra):
        if palavra[x] in 'aeiou':
            
            return palavra[x]
        else: 
            s=s+palavra[x]
        x=x+1
    return s