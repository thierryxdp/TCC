def soma_h(numero):
    lista = []
    if numero%2==0:
    	for x in range(1,numero+1,2):
        	somar = (1/x)+(1/(x+1))
        	lista.append(somar)
        return round(sum(lista),2)
    else:
        for x in range(1,numero,2):
            somar = (1/x)+(1/(x+1))
            lista.append(somar)
        return round(sum(lista),2)