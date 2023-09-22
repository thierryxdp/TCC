def soma_h(n):
    """Função que calcula e retorna o valor H com N termos onde N é inteiro
    e dado como  entrada. Retorna o resultado só com 2 casas decimais, usando
    a funçao  round(n°, 2);
    int -> float"""
    acumulador = 0
    for i in range(1, n + 1):
        H = 1 / i
         acumulador += H
            
    return round(acumulador, 2)