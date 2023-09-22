def soma_h(numero):
    lista = []
    for x in range(1,numero+1,2):
        if numero%2==0:
        	somar = (x**-1)+((x+1)**-1)
        	lista.append(somar)
    	else:
            somar = (x**-1)+((x+1)**-1)
            lista.append(somar)
            lista.append(numero**-1)
    return lista