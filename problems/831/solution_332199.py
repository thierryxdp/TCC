def lingua_p(palavra):
    soma=''
    vogal='aeiou'
    for i in range(len(palavra)):
        if palavra[i] not in vogal:
            soma=palavra+soma
        if soma in vogal:
            soma=str.replace(vogal,'p',vogal)
    return soma