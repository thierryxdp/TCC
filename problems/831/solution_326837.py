def lingua_p(palavra):
    a='AEIOUaeiou'
    i=0
    for x in range(len(palavra)):
        if palavra[i] in a:
             str.replace(palavra,palavra[i]'p'palavra[i],i,i)
        i+=1       
    return palavra