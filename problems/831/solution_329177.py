def lingua_p(palavra):
    '''Recebe uma palavra e a retorna na língua do p
    str->str'''
    vogais='AEIOUaeiou'
    i=0
    quantidade=len(palavra)
    for letra in palavra:
        if letra in vogais:
            palavra_p=palavra[0:i]+letra+palavra[i+2:quantidade]
        i=i+1
    return palavra_p