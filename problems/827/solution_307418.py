def qtd_divisores(numero):
    lista = ()
    i = 1
    while i < numero:
        if numero%i==0:
        	lista = lista + (i)
        i = i + 1
    return lista