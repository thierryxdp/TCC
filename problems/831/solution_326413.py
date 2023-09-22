def lingua_p(palavra):
    str_nova=''
    for letra in palavra.lower():
        if letra in 'aeiou':
            str_nova+= letra+'p'+letra
        else:
            str_nova+=letra
    return str_nova