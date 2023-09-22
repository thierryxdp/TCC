def lingua_p(palavra):
    
    palavra.lower()
    vogal='aàáâãeéêiíoóõôuú'
    i=0
    string=str()
    for vogal in palavra:
        string = palavra[i] + 'p' + palavra[i]
        i+=1
    return palavra