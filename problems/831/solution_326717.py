def lingua_p(palavra):
    i=0
    p =''
    for i in range(len(palavra)):
        if palavra[i] in 'AEIOUaeiou':
            p= p+palavra[i]+'p'
            i+1
    return p