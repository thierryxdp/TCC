def substitui(string,caractere,numero):
    # Recebe uma string, um número correspondente a posição de um caractere, e um caractere para substituir este.
	# string, string, int -> string
  	return string[0:numero]+caractere+string[numero:-1]