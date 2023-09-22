def lingua_p(palavra):
    palavra_comP='' 
    vogais='AEIOUaeiou'
    for letra in palavra:
        if letra in vogais:
            palavra_comP=palavra_comP+letra+'p'+letra
        else:
            palavra_comP=palavra_comP+letra
    return palavra_comP.lower