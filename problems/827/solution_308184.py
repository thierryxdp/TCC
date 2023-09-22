def qtd_divisores(num:int)->int:
    """Função que conta quantos divisores um número tem."""
    num=list(range(num,0,-1))
    divisores=0
    for elemento in num:
        if max(num)%elemento==0:
            divisores+=1
    return divisores