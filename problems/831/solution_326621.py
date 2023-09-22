def lingua_p(palavra):
    
    palavra.lower()
    vogal='aàáâãeéêiíoóõôuú'
    string=str()
    i=0
    for i in palavra:
        if vogal:
            string = palavra[:i]+ palavra[i] + 'p' + palavra[i]+ palavra[i:]
        else:
            string=''
        i+=1    
    return palavra