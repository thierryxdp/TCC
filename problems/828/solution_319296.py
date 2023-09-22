def primo(numero):
    ''' retorna se um número inteiro é primo ou não.
    int -> boolean'''

    contagem = 0
    divisores = []

    for i in range(2,numero):
        if (numero%i) == 0:
            contagem = contagem + 1
    return (contagem < 1)