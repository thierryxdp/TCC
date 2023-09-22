def soma_h(numero):
    lista = []
    for x in range(1,numero+1,2):
        if numero%2==0:
        	somar = (x**-1)+((x+1)**-1)
        	lista.append(somar)
            return roun(sum(lista),2)
    	else:
            somar = (1/x)+(1/(x+1))
            lista.append(somar)
            
    return sum(lista)