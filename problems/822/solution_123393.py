# Dada uma lista de números, esta função retorna o número de vezes que um
# elemento da lisat é igual ao seu anterior nesta mesma lista.
# list -> int
def analisar_fatias(fatia):
	for i in range(1, len(fatia)+1):
        if fatia[i] == fatia[i-1]:
            return True
        else:
            return False
       
    
# Dada uma lista de números, esta função retorna o número de vezes que um
# elemento da lisat é igual ao seu anterior nesta mesma lista.
# list -> int

def repetidos(lista):
    cont = 0
    
    cont = filter(analisar_fatias,lista)

    return cont

    cont = 0