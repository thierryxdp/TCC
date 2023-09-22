def primo(numero):
    """funcao que dado um numero inteiro positivo de entrada,
    verifica se este numero e primo ou nao e retorne um valor
    booleano;
    int -> bool"""
    
    divisores = []
    for i in range(1,numero + 1):
        if numero%i ==0:
            divisores = divisores + [i]
        i = i +1
    return len(divisores) = 2: