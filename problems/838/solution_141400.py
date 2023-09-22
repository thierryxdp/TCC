'''A função num_bombons aceita 2 floats ou integers como parâmetros: O primeiro
	define a quantidade de dinheiro que o usuário pode gastar,
    e o segundo quanto cada bombom custa. Ela retorna o integer ou float 
    quantidade, que representa a quantidade bombons que podem ser 
    comprados com o saldo disponível.'''
def num_bombons(saldo, preco):
    '''O número de bombons que Pedrinho pode comprar se dá
    pela quantidade de dinheiro que ele tem dividida pelo preço
    individual dos bombons.'''
    quantidade = saldo // preco
    return quantidade