def lingua_p(palavra):
    palavra_em_p: ''
    for letra in palavra:
        if letra in 'aeiouãáâéíóõúAEIOUÃÁÂÉÍÓÕÚ':
            palavra_em_p += palavra[: index(letra) +1] + 'p' + letra
        else:
            palavra_em_p += palavra[: index(letra) +1]
    return palavra_em_p