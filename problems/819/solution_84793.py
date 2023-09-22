def filtraMultiplos(lista,n):
    'função que recebe lista de números e número n e retorna lista com múltiplos de n. lista, int->lista'
    multiplos=[]
    indice=0
    while indice<=len(lista):
        if lista[indice]%n==0:
            #multiplos+=lista[indice]
        	list.append(multiplos,lista[indice])
        indice+=1
    return multiplos