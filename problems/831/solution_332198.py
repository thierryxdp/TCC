def lingua_p(palavra):
    soma=''
    vogal='aeiou'
    for string in range(len(palavra)):
        if soma not in vogal:
            soma=palavra+soma
        if soma in vogal:
            soma=str.replace(vogal,'p',vogal)
    return soma