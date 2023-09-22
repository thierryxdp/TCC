def primo(numero_inteiro):

    """ Esta função nos fornece um valor booleano que indica
        se o numero inteiro fornecido na função é primo ou não.
        Para ser primo, um número deve ter dois divisores não iguais e positivos.
        Usaremos a função que calcule quantos divisores um número inteiro
        possui para nos auxiliar.
        int -> bool
    """

    qtd_divisores = 0

    for n in range(1,numero_inteiro+1):
        if numero_inteiro%n == 0:
            qtd_divisores = qtd_divisores + 1

    if qtd_divisores == 2:
        return True

    else:
        return False