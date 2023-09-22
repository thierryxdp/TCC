#
#
#
#
def lingua_p(palavra):
    palavra_p=0
    for letra in palavra:
        if letra in 'AEIOUÁÀÃÉÍÓÔÕUÚaeiouáàãéíóôõuú':
            palavra_p=palavra_p+letra+'p'+letra
        palavra_p=palavra_p+letra
    str.lower(palavra_p)
    return palavra_p