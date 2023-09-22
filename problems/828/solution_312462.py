def primo(numero):
    'Dado um número, retorna a quantidade de divisores que este número possui. Entrada: int. Saída: int.'
    resultado=0
    for divisor in range(1,numero+1):
        if numero%divisor==0:
            resultado=resultado+1
    if resultado<3:
        return True
    else:
        return False