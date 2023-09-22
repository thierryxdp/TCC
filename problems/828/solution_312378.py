def primo_n (numero):
    """funçao que recebe um numero inteiro e retorna true se ele é um numero primo e false se nao;
    entrada: int;
    saida: bool."""
    if n % 2 == 0:
        return False
    for elemento in range (3,n,2):
        if n % elemento == 0:
            return False
    return True