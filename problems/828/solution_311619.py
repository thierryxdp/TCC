def primo(numero):
    """A funcao primo recebe como entrada um numero inteiro qualquer e
    calcula o numero de divisores deste, para que retorne a seguinte informacao
    booleana: se o número de divisores é igual a 2. Se for, é primo."""
    divisores = 0
    for indice in range(1,numero + 1):
        if numero%indice == 0:
           divisores = divisores + len([indice])
    return bool(divisores == 2)