def posLetra(text, letra, num):
    """Recebe e retorna o index em qual esta a repeticao num de uma determinada
    letra em um texto;
    str, str, int --> int"""

    iii = 0
    cont = 0

    while ((iii < len(text)) and cont != num ):
        if (text[iii] == letra):
            # Conta quantas vezes a letra apareceu
            cont += 1
            
        iii += 1
	if (cont == 0):
    	return -1
    return iii