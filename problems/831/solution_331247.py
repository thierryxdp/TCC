def lingua_p(palavra):
    "recebe uma palavra e a traduz para a lingua do P"
    for letra in palavra:
        if letra in ['a','e','i','o','u']:
            letra = letra + 'p' + letra
    return palavra