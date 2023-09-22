def qtd_divisores(n):
    """Recebe como entrada um número "n" e retorna a quantidade de divisores positivos de "n";int->int"""
    num=0
    for valor in range(n):
        if n%(int(valor)+1)==0:
            num=num+1
    return num