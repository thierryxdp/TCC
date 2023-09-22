def qtd_divisores(numero):
    """Retorna a quantidade de divisores do numero;
    	int -> int"""
    lista = []
    i = 1
    while i <= numero:
        if numero%i==0:
        	lista = lista + [i]
        i = i + 1
    return len(lista)