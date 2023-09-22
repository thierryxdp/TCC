def lingua_p(palavra):
    p=0
    vogais='AEIOUaeiou'
    for i in palavra:
        if i in vogais:
            p=p+i+'p'
        else:
            p=p+i
    return p