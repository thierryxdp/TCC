def substitui(string,caractere,numero):
    # Recebe uma string, um número correspondente a posição de um caractere, e um caractere para substituir este.
    # Utiliza o fatiamento de strings para unir a parte antes do do caractere a ser substituído, o novo caractere,
    # e o resto da string após o caractere.
	# string, string, int -> string
  	return string[0:numero]+caractere+string[numero+1:]