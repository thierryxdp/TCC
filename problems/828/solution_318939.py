def primo(x):
    """Dada uma funcao que dado um numero inteiro positivo, verifica se este numero
    e primo ou nao. retorna um valor booleano. Entrada: int,-->bool"""
    r = 0
    for i in range(x):
        if x%(i+1) == 0:
            r = r + 1
	if r>2:
        return False
    elif r<i:
        return True