def faltante(L):
    """função que dad auma lista com N números inteiros - 1, retorna o numero do intervalo da lista que está faltando
	list -> int"""
    
    lista = sorted(L)
    
    for i in range(len(lista)):
        while i + 1 != lista[i]:
            return i + 1
        
	return len(lista) + 1