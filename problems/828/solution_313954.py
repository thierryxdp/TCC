def primo(n):
    """ dado um numero, calcula se ele é primo ou não, 
    retorna True caso seja e False caso não seja;
    int -> bool"""
    resposta = 0
    for numero in range(1, n+1):
        if n % numero == 0:
            resposta += 1
    return resposta == 2