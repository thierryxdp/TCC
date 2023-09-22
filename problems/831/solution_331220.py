def lingua_p(palavra):
    palavra_p = []
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            palavra_p = palavra_p + list(letra) + list('p')
        else:
            palavfa_p = palavra_p = list(letra)
        return palavra_p