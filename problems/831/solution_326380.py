def lingua_p(palavra):
    
    palavra.lower
    vogal='aàáâãeéêiíoóõôuú'
    i=0
    for vogal in palavra[i]:
        palavra[i] = palavra[i] + 'p' + palavra[i]
        i+=1
    return palavra