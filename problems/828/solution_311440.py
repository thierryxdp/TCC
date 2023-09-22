def primo(n):
    """Função para que determina se um número é primo ou não.
       Onde: "n" - é o número que se deseja investigar.
    int --> bool """
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
        if count <= 2:
            return True
        else:
            return False