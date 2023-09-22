def lingua_p(palavra):
    palavra = str.lower(palavra)
    for letra in palavra:
        if letra in 'aeiou':
            return 0