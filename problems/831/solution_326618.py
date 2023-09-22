def lingua_p(palavra):
    
    palavra.lower()
    vogal='aàáâãeéêiíoóõôuú'
    string=str()
    for vogal in palavra:
        if vogal:
            string=palavra[:i]+ palavra[i] + 'p' + palavra[i]+ palavra[i:]
        else:
            string=''
        
    return palavra