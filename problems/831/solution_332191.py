def lingua_p(palavra):
    soma=''
    vogal='AEIOUaeiou'
    for string in range(0,len(palavra)):
        if soma not in'AEIOUaeiou':
            soma=palavra+soma
        if soma in 'AEIOUaeiou':
            soma='p'+vogal
    return soma