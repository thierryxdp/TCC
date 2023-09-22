def lingua_p(palavra):
    
    trecho=''
    for vogal in palavra:
        if vogal in "aeiou":
            trecho=vogal+'p'
    return palavra