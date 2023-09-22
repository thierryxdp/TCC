def posLetra(stringue,letra,numero):
	"""retorna a posicao da string q a ocorrencia da letra ta, caso
    exita menos ocorrencias retorna -1"""
    contador = 0
    resposta = 0
    if str.count(stringue,letra)<numero:
        return -1
    while contador < numero:
        if str.count(stringue,letra) == numero:
        	resposta = str.find(stringue,letra,contador)
            contador +=1
        if str.count(stringue,letra)> numero:
            resposta = str.find(stringue,letra,0,numero
            contador+= 
    return resposta