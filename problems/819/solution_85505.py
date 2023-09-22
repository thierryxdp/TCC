def filtraMultiplos(lista,n):
    '''função recebe uma lista com inteiros, um número e retorna
    os elemtnos da lista que forem divisiveis pelo mesmo
    list int --> int'''
    i=0
	resultado=[]
	while i<len(lista):
        if lista[i]%n==0:
            list.append(resultado,lista[i])
        i=i+1
    return resultado