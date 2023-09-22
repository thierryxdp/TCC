def primo(n:int)->bool:
    """dado um numero inteiro positivo, verifica  se este numero é primo
ou n˜ao e Retorna um valor booleano"""
    ponto_parada = round(n**(1/2)) + 1
    for i in range(2, ponto_parada):
        if n % i == 0:
            return False
    return True