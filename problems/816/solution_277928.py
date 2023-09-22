def maiores(lista_inteiros,n):
    #Essa funçao dada um lista de numeros int e um numero n ,retorna outra lista com
    #numeros maiores que n o dada lista original
    list.insert(lista_inteiros,0,n)
    list.sort(lista_inteiros,reverse=True)
    x = list.index(lista_inteiros,n,0)
    del lista_inteiros[x::]