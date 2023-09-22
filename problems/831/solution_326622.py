def lingua_p(palavra):
    
    palavra.lower()
    vogal='aàáâãeéêiíoóõôuú'
    string=str()
    for i in palavra:
        if vogal:
            string = i + 'p' + i 
        else:
            string=''   
    return palavra