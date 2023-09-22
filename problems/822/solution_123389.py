# Dada uma lista de números, esta função retorna o número de vezes que um
# elemento da lisat é igual ao seu anterior nesta mesma lista.
# list -> int
def analisar_fatias(fatia):
	for i in range(len(fatia)+1):
        if fatia[i] == fatia[i-1]:
            resp = True
        else:
            resp = False
    return resp

def repetidos(lista):
    cont = 0
    
    cont = sum(filter(analisar_fatias,lista))

    return cont