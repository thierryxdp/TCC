def primo(numero):
    """dado um número inteiro positivo,
verifica se este número é primo
ou não. Retorna um valor booleano"""
    divisores = []
    i = 0
    nova = list(range(1,numero+1)) #a partir do numero 1 para não dar esse no proximo passo

    while i < len(list(range(numero))):
        if numero%nova[i] == 0: #caso comece no zero, dará erro
            divisores += [i+1]

        i += 1

    if len(divisores) == 2: #2, pois ele é divisivel por 1 e ele mesmo
        return True

    else:
        return False