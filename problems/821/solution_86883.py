def fatorial(numero):
    """Função que dado um numero, calcule o fatorial deste numero.
    int -> int."""
    
    indice = 1
    fat = 1
    while indice < numero:
        fat = fat*(indice + 1)
        indice += 1
	return fat