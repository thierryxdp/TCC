def soma_h (numero):
    """funçao que recebe um numero inteiro divide por 1 de 1 ate o numero e retorna o somatorio das divisoes;
entrada: int;
saida: float."""
    soma = 0
    for elemento in range (1, numero+1):
        soma += (1/elemento)
    return round (soma, 2)