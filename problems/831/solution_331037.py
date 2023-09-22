def lingua_p(palavra):
    p=''
    vogais='AEIOUaeiou'
    for i in palavra:
        if i in vogais:
            p=p+i+'p'+i
        else:
            p=p+i
    return p