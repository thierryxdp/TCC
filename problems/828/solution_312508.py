def primo(n):
    """Esta função recebe um número e verifica se ele é um número primo
    int -> bool"""
    lista = [ ]
    for i in range(1,n+1):
        if n%i == 0:
            lista.append(i)
    if len(lista) == 2:
        return True
	else:
        return False