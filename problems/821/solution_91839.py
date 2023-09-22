def fatorial(numero):
    '''retorna o fatorial do numero pedido
    int -> int'''
    if numero == 0:
        return 1
    elif numero < 0 :
        return 'nao existe fatorial'
    else:
        fatorial = 1
        while numero > 1:
            fatorial *= numero
            numero -= 1
	return fatorial