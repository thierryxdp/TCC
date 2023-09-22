def lingua_p(palavra):
    a='AEIOUaeiou'
    i=0
    str.split(palavra)
    for x in palavra:
        if palavra[i] in a:
             palavra[i]+='p'+palavra[i]
        i+=1
    return palavra