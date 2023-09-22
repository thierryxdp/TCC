def lingua_p(palavra):
    a='AEIOUaeiou'
    i=0
    b=()
    str.split(palavra)
    for x in palavra:
        if palavra[i] in a:
             b=list.insert(palavra,i+1,'p'+palavra[i])
        i+=1
    return str.join(' ',palavra)