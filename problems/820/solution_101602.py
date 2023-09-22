def posLetra (frase,letra,numero):
    """
    	string,string,int -> int
    """
    i = 0
	ocorrencias = frase.count(letra)
    if ocorrencias<numero:
        return -1
    elif numero==1:
        posicao = frase.find(letra) if numero==1
        return posicao
    else:
        posicao = frase.rfind(letra)
        return posicao