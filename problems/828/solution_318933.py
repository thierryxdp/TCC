def primo(x):
    """Dada uma funcao que dado um numero inteiro positivo, verifica se este numero
    e primo ou nao. retorna um valor booleano. Entrada: int,-->bool"""
    s = 0
    for i in range(x):
        if x%(i+1) == 0:
            s = s + 1
        if s>2:
            return False
        elif s<i:
            return True