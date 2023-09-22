def maiores(lista,n):
    

    if  n >= min(lista) and n<=max(lista):
        nova_lista = [n] + lista
        nova_lista.sort(reverse = False)

        return nova_lista


    if n >= max(lista):
        nova_lista = []
        return nova_lista