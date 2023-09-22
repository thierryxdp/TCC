def lingua_p(palavra):
    soma=''
    vogal='AEIOUaeiou'
    for string in range(0,len(palavra)):
        if soma not in vogal:
            soma=palavra+soma
        if soma in vogal:
            soma=str.replace('p',vogal)
    return soma