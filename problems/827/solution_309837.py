def qtd_divisores(n):
    """Retorna quantos divisores um dado número inteiro
tem.
assinatura: int --> int
casos de teste:
qtd_divisores(0) == 0
qtd_divisores(5) == 2
qtd_divisores(10) == 4
qtd_divisores(-2) == 0
"""
    d = 0
    if(n>0):
        for i in range(1, 10000):
            if(n%i == 0):
                d+=1
        return d
    else:
        return 0