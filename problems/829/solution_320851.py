def soma_h (n) :
    """Funcao que calcula e retorna o valor 'h' com 'n' termos onde 'n' e inteiro e dado como entrada"""
    contador = 0
    for i in range(1, n+1) :
        if n%i == 0:
            contador += 1.0/i
    return contador