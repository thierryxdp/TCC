def maiores(Numeros_lista,n):
    '''funcao que dada uma lista e um numero n, retorna '''
    if n not in Numeros_lista:
        Numeros_lista.append(n)
        Numeros_lista.sort()
        i =Numeros_lista.index(n)
        sublista = Numeros_lista [i+1:]
        rep = sublista.count(n)
        return sublista[rep:]