def posLetra(frase, letra, ocorrencia):
    """funcao que recebe uma stringa, letra e um numero que indica a ocorrencia desejada da letra e
	retorna a posição da string onde está a ocorrencia da letra, caso exista menos ocorrencias do que o pedido
	retorna -1
	str, str, int -> int"""
    
    i = 0
    n = 0
    while i < len(frase):
        if frase[i] == letra:
            n = n + 1
		i = i + 1
	
    if n > ocorrencia: 
        return n
    
    else: 
        return -1