def lingua_p(palavra):
    a='AEIOUaeiou'
    i=0
    b=palavra
    for x in palavra:
        if b[i] in a:
             list.insert(b,i+1,'p'+b[i])
        i+=1
    return palavra