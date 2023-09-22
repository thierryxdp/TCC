def lingua_p(palavra):
    
    palavra.lower()
    vogal='aàáâãeéêiíoóõôuú'
    i=0
    string=str()
    for vogal[i] in palavra[i]:
        string = palavra[i] + 'p' + palavra[i]
        i+=1
    return palavra