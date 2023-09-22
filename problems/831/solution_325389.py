def lingua_p(palavra):
    s = ''
    x=0
    while x<len(frase):
        if frase[x] in 'aeiou':
            s=s+frase[x+1].index(p)
            s=s+frase[x-1].index(p)
        else: 
            s=s+frase[x]
        x=x+1
    return s