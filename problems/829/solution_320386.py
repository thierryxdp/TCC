def soma_h(numero):
    lista = []
    for x in range(1,numero+1,2):
    	somar = round((x**-1)+((x+1)**-1),2)
        lista.append(somar)
    return sum(lista)