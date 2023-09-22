def lingua_p(p):
    linguap=''
    for x<len(p):
        if p in 'aeiou':
            linguap = linguap + 'p'
        else:
            linguap = linguap + p
    return linguap