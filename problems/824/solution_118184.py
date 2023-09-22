def ultima(d):

    i=0
    vogal=''
    while i<len(d):
        if d[i] in 'AEIOUaeiou':
             vogal=d[i]
        i=i+1

    return vogal