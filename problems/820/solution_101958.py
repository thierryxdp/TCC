def posLetra(stringue,letra,numero):
	"""retorna a posicao da string q a ocorrencia da letra ta, caso
    exita menos ocorrencias retorna -1"""
    contador = 0
    resposta = 0
    conta2 = 0
    
    if numero == 1:
        return str.find(stringue,letra)
    if str.count(stringue,letra)<numero:
        return -1
    while contador < numero:
        if str.count(stringue,letra) == numero:
        	resposta = str.find(stringue,letra,contador)
            contador = contador + 1
        elif str.count(stringue,letra)> numero:
            resposta = str.find(stringue,letra,0,numero)
            contador = contador +1
    while resposta < numero:
        resposta = str.find(stringue,letra,resposta)
        conta2 +=1
    return resposta