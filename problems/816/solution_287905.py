def maiores(lista):
    lista = [a, b, c, d]
    n = 1
    lista_final = []
    for elemento in lista:
        if elemento > n:
            lista_final.append(elemento)
            return(lista_final)