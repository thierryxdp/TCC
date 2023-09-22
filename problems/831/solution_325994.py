def lingua_p(palavra):
    nova_Palavra = ''
    for letra in palavra:
        if letra in "aeiouAEIOU":
            nova_Palavra += letra + "p" + letra
    	return nova_Palavra