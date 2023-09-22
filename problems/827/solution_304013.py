def qtd_divisores(n):
    """Recebe como entrada um número "n" e retorna a quantidade de divisores positivos de "n";int->int"""
    num=0
    for valor in range(n):
        if (valor+1)%n==0:
            num=num+1
    return num