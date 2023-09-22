#
#
#
#
def lingua_p(palavra):
    palavra_p=''
    for letra in palavra:
        if letra in 'AEIOUÁÀÃÉÍÓÔÕUÚaeiouáàãéíóôõuú':
            palavra_p=palavra_p+letra+'p'
        palavra_p=palavra_p+letra
    str.lower(palavra_p)
    return palavra_p