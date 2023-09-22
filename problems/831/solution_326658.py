def lingua_p(palavra):
    vogal= 'AEIOUaeiou'
    p =''
    for i in range(palavra):
        if i in vogal:
            p = i+'p'
    return p