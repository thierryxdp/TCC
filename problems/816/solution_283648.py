def maiores(lista,n):

    num_maiores=[x for x in lista if x > n]
    list.sort(num_maiores)
    
    return num_maiores