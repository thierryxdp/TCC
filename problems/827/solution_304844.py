def qtd_divisores (n: int) -> int:
    """Retorna quantos divisores o numero inteiro n possui."""
    divisores=[1,n]
    i=2
    if n<0:
        return 0
    else:
        while i<=n/2:
            if n%i == 0:
                divisores.append(i)
            i+=1
    qtd_de_divisores=len(divisores)
    return qtd_de_divisores