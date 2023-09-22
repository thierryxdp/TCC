def bolos(quantidade_farinha, quantidade_ovo, quantidade_leite):
    bolos_farinha = farinha // 2
	bolos_ovo = ovo // 3
	bolos_leite = leite // 5
	if bolos_farinha <= bolos_ovo and bolos_farinha <= bolos_leite:
        return bolos_farinha
	elif bolos_ovo <= bolos_farinha and bolos_ovo <= bolos_leite:
        return bolos_ovo
    else:
        return bolos_leite