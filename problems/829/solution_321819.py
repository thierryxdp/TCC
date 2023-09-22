def soma_h(n):
    """Calcula e retorna o valor H com N termos onde N é inteiro e dado com entrada.
    int -> int"""
    h = 0
    t = n
    for i in range(t+1):
        if i != 0:           
        	h = h+(1/i)
    return round(h,2)