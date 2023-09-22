def lingua_p(palavra):
    
    trecho=''
    for vogal in palavra:
        if vogal in "aeiou":
            vogal=vogal+'p'
        
    return palavra