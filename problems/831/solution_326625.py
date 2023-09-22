def lingua_p(palavra):
    
    palavra.lower()
    vogal='aàáâãeéêiíoóõôuú'
    string=str()
    for i in palavra:
        if i in vogal:
            string += i + 'p' + i 
        else:
            string+=i
    return string