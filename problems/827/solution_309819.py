def qtd_divisores(num):
    """Recebe um número e retorna o número de divisores que ele tem.
    assinatura: int --> int
    testes:
    """
    contador = 0
    if num > 0:
        for i in range(1, 10000):
            if num%i == 0:
                contador = contador + 1
        return contador
    
    if num < 0:
        return 0