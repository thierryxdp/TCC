def filtraMultiplos(lista_num,n):
    contador_indices=0
    multiplos=[]
    while contador_indices<len(lista_num):
        if lista_num[contador_indices]%3==0:
            multiplos.append(lista_num[contador_indices])
        contador_indices+=1
    return multiplos