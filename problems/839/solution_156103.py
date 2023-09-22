def carros(n, c = 5):
    """Dados o numero de pessoas e a capacidade de um veículo, calcula a quantidade de veiculos necessarios para o transporte das pessoas
    int, int -> int"""
    if c == False and n%c > 0:
        return (n//5) + 1
    elif c == False and n%c == 0:
        return n/5
    elif c > 0 and n%c > 0:
        return (n//c) + 1
    else:
        return (n/c)