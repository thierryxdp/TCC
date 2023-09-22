def lingua_p(palavra):
    
    trecho=''
    for vogal in palavra:
        if vogal in "aeiou":
            palavra=vogal+'p'
    return palavra