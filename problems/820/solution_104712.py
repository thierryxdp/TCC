def posLetra(frase,letra,num):
    """Retorna o indice da ocorrencia da letra, dadas por parametro, na frase ;
    str,str,int -> int"""
    cont = 0
    vez = 0
    retorno = -1
    while cont < len(frase):
        if letra == frase[cont]:
            vez += 1
        if vez == num:
            retorno = cont
        cont += 1
	return retorno