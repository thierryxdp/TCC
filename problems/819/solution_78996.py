def filtro(num):
    """Verifica que se num é divisível por n"""
	global n 
    return num % n == 0

def filtraMultiplos(lista, numero):
    """Função que, dada uma lista de números e um número, retorna outra lista contendo
    todos os números divisíveis pelo número."""

    return list(filter(lambda num:num%n == 0, lista))