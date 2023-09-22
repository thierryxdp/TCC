def filtraMultiplos (lista_numeros,n):
    '''retorna outra lista contendo todos elementos da lista original que forem divisíveis por n;
list,int->list'''
    i=0
    lista=[]
    while i<len(lista_numeros):
        if lista_numeros[i]%n==0:
            lista.append(lista_numeros[i])
        i+=1
            return lista