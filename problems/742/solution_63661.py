def substitui(string,caractere,numero):
    # Recebe uma string, um número correspondente a posição de um caractere, e um caractere para substituir este.
	# string, int, int -> string
  	return string(0:numero)+caractere+string(caractere:-1)