def posLetra(frase,letra,num):
    """Função que ao receber uma frase, letra e um número, este número
    indica a ocorrência desejada da letra, retornando a posição exata
    em que esta letra se encontra na frase;
    str, str, int -> int"""
    contador = 0
    pos = 0
    i = 0
    while i < len(frase):
        if frase.count(letra) < num:
            pos = -1
        else:
            if frase[i] == letra:
                contador += 1
                if contador == num:
                    pos = i
		i+=1
	return pos