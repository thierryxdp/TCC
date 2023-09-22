def primo (numero):
    """funçao que recebe um numero inteiro e retorna true se ele é um numero primo e false se nao;
    entrada: int;
    saida: bool."""
    if numero % 2 == 0:
        return False
    for elemento in range (3,numero,2):
        if numero % elemento == 0:
            return False
    return True