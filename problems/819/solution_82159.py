lista = [8, 9, 5, 6, -2, -7, -9, -6, -3, -4, 12, 14, 90, 75, 65]
def maior_que_zero(num):
    '''Função que filtra os numeros maiores que zero;
    int -> int'''
    if num > 0:
        return True
    else:
		return False
lista_valida = filter(maior_que_zero, lista)
print lista_valida