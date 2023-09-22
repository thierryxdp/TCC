def primo(n):
    """Função que recebe um inteiro positivo 
    e verifica se é primo ou não, retornando um 
    valor booleano. int -> bool"""
    cont = 0
    for x in range(1, n+1):
        if n % x == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False