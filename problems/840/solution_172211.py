def bolos(a,b,c):
    bolos_farinha = a // 2
    bolos_ovo = b // 3 
    bolos_leite = c // 5
    if bolos_farinha <= bolos_ovo and bolos_farinha <= bolos _leite :
        return bolos_farinha
    elif bolos_ovo <= bolos_farinha and bolos_ovos <= bolos_leite:
        return bolos_ovo
    else:
        return bolos_leite