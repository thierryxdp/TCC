def posLetra(frase,letra,ocorrencia):
    """funçao que recebe uma frase, uma letra e um numero que indica a ocorrencia desejada da letra na frase e retorna a posiçao onde a letra esta na str, se ocorrencia < numero de ocorrencias na str retorna -1.
    entrada: str, str, int;
    saida: int."""
    
     totaldeocorrencia = str.count(frase, x)
    if n > totaldeocorrencia:
        return -1
    
    elif n<= totaldeocorrencia:
        contador=0
        acumulador=[0]
        while contador < len (frase):
            if x == frase [contador]:
                acumulador =acumulador + [contador]
	    contador = contador + 1
	    return acumulador [n]