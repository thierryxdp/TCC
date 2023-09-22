def filtraMultiplos(lista,n):
    """funcao que recebe como entrada uma lista de numeros e um numero n,
    e retorna uma outra lista contendo todos os elementos da lista original
    multiplos de n;
    list, int -> list"""
    lista_multiplos=[]
    contador=0
    while contador<len(lista):
        if lista[contador]%n==0:
            lista_multiplos+=[lista[contador]]
    contador+=1
    return lista_multiplos