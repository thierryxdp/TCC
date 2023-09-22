def qtd_divisores(n :int) -> int:
    """Conta quantos divisores um dado número inteiro tem.
    Exemplo: Se o número for 10, os divisores são: 1, 2, 5 e 10; total de 4 divisores"""
    
    
    divisores = []
    for i in range(1, n + 1):
        if i % n == 0:
            list.extend(divisores, n)
    return len(divisores)