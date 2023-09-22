def qtd_divisores(n):
    """Função para determinar a quantidade de divisores de um número.
       Onde: "n" - é o número que se deseja saber a quantidade de divisores.
    int --> int """
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1
     return divisores