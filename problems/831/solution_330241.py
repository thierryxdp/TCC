def lingua_p(palavra):
    linguaP = ()
    
    for letra in palavra:
        if palavra[letra] in "AEIOUaeiou":
            linguaP=+ palavra[letra] + p + palavra[letra]
        else:
            linguaP=+ palavra[letra]
    return linguaP