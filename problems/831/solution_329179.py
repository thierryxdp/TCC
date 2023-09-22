def lingua_p(palavra):
    '''Recebe uma palavra e a retorna na língua do p
    str->str'''
    vogais='AEIOUaeiou'
    i=0
    quantidade=len(palavra)
    for letra in palavra:
        if letra in vogais:
            palavra_p=palavra_p+letra+'p'
        elif letra not in vogais:
            palavra_p=palavra_p+letra
    return palavra_p