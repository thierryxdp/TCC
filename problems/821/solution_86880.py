def fatorial(numero):
    """Função que dado um numero, calcule o fatorial deste numero.
    int -> int."""
    
    indice = 0
    fat = 3
    while indice < numero:
        fat = fat*(fat - 1)
        indice += 1
	return fat