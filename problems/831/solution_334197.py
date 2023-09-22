def lingua_p(palavra):
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            palavra.replace(letra, (letra+'p'+letra))
    return palavra