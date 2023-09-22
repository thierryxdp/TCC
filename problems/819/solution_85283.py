def filtraMultiplos(lista,n):
    '''dada uma lista de numeros e um numero, retorna outra lista com apenas os numeros da lista original que sejam multiplos do numero dado como parametro; list,int -> list'''
    i = 0
    nova_lista = []
    while i<len(lista):
        if lista[i]%n == 0:
            nova_lista = nova_lista + [lista[i]]
        else:
            nova_lista = nova_lista
        i = i + 1
    return nova_lista