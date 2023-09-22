def filtra_pares(t):
    lista=[]
    for i in t:
        if type(i) != int:
                lista = []
                break
        elif i%2 == 0: 
            lista.append(i)
            return(tuple(lista))