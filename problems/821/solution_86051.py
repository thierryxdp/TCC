def fatorial(num):
    """Calcula e Retorna o fatorial do número dado;
       int->int
       Parâmetros:
       num: número inteiro qualquer
    """
    fatorial=1
    while num>=1:
        fatorial=fatorial*num
        num=num-1

    return fatorial