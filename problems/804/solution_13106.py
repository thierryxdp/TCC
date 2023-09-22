#Dado uma de quatro elementos inteiros, retorna uma tupla com os elmentos pares da tupla originaint,int,int,int(tupla)--> int(tupla)
def filtra_pares(tupla):
    tuplaN = ()
    if tupla[0] %2 == 0:
    	tuplaN = tuplaN + (tupla[0],)
    if tupla[1] %2 == 0:
    	tuplaN = tuplaN + (tupla[1],)
    if tupla[2] %2 == 0:
    	tuplaN = tuplaN + (tupla[2],)
    if tupla[3] %2 == 0:
    	tuplaN = tuplaN + (tupla[3],)
    return tuplaN