def soma_h (n) :
    """funcao que calcula e retorna o valor 'h' com 'n'"""
    contador = 0
    for i in range(1, n+1) :
        contador += 1.0/i
        return round( contador,2)