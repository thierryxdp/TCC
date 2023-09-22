def posLetra(string, letra, numero):
    """retorna em que posição da string aquela ocorrencia da letra esta. str, str, int -> int"""
    a=str.count(string,letra)
    if a-numero<0:
        return -1
    else:
        b=str.find(string,letra)
    	return b