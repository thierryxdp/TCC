def fatorial(numero):
    '''retorna o fatorial do numero pedido
    int -> int'''
    if numero == 0:
        return 1
    elif numero < 0 :
        return 'nao existe fatorial'
    else:
        resposta = numero
        while numero > 1:
            resposta = resposta * 1
            resposta = numero - 1
	return resposta