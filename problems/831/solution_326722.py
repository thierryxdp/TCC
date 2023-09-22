def lingua_p(palavra):
    i=0
    p =''
    for i in range(len(palavra)):
        if palavra[i] in 'AEIOUaeiou':
            p= p+'p'+palavra[i]+'p'
        else:
                p=p+palavra[i]
        i+1
    return p