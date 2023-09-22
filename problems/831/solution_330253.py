def lingua_p(palavra):
    linguaP = ''
    
    for letra in palavra:
        if letra in "AEIOUaeiou´":
            linguaP = linguaP + (letra) + ('p') + (letra)
        else:
            linguaP = linguaP + (letra)
    return linguaP