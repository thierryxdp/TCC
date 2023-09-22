def lingua_p(palavra):
    '''Recebe uma palavra e a retorna na língua do p
    str->str'''
    vogais='AEIOUaeiouáéíóúãõâêôÁÉÍÓÚÃÂÊÔ'
    quantidade=len(palavra)
    palavra_p=''
    for letra in palavra:
        if letra in vogais:
            palavra_p=palavra_p+letra+'p'+letra
        elif letra not in vogais:
            palavra_p=palavra_p+letra
    return palavra_p