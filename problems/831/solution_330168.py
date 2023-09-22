def lingua_p(palavra):
    palavra_nova = []
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            palavra_nova = letra+'p'+letra
        if letra not in 'AEIOUaeiou':
            palavra_nova = letra
    return str.lower(palavra_nova)