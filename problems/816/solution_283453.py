def maiores(lista,n):
    """Retorna os numeros da lista maiores do que o selecionado;
    	list,int -> list"""
    list.insert(lista,0,n)
    list.sort(lista)
    x = list.index(lista,n)
    return lista[x+1:]