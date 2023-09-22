def lingua_p(palavra):
    palavra = str.lower(palavra)
    nova_palavra = ''
    for letra in palavra:
        #Inserindo o p pela incidência de vogal
        if letra in 'aeiouéáàèùúíì':
            nova_palavra = nova_palavra + letra + 'p' + letra
        else:
            nova_palavra = nova_palavra + letra
	return nova_palavra