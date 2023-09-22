def lingua_p(palavra):
    
    palavra.lower
    vogal='aàáâãeéêiíoóõôuú'
    for palavra[i] in vogal:
        palavra[i] = palavra[i] + 'p' + palavra[i]
    return palavra