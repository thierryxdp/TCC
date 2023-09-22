def carros(p):
    """Função que calcula a quantidade de veículos necessários para transportar o número de pessoas p; int -> int."""
    if p<=5:
        return 1
    if p>5:
        return round(p/5)
    if p==0:
        return 0