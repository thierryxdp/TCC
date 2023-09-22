def lingua_p(palavra):
    soma=''
    vogal='a' or 'e' or 'i' or 'o' or 'u'
    for i in range(len(palavra)):
        if palavra[i] not in vogal:
            soma=palavra
        if palavra[i] in vogal:
            soma=str.replace(vogal,'p',vogal)
    return soma