def soma_h(numero):
    lista = []
    if numero%2==0:
        for i in range (1,numero+1,2):
            somar = (1/i)+(1/(i+1))
            lista.append(somar)
 		return round(sum(lista),2)
    else:
        for i in range(1,numero,2):
            somar = (1/i)+(1/(i+1))
            lista.append(somar)
        return round(sum(lista)+1/numero,2)