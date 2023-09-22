def soma_h(n):
    lista = list(range(0, n+1))
    lista2 = []
    for i in lista:
        if i > 1:
            b = 1/lista[i]
            lista2 = lista2 + [b]
        else: i+=1    
    return round(sum(lista2)+1, 2)