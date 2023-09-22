def maiores(lista,n):
    """Função que dada uma lista de numeros inteiros e um inteiro n, 
    retorna outra lista que contem todos os numeros da lista original
    maiores que n;list,int-->list"""
    if n not in lista:
        list.append(lista,n)
    list.sort(lista)
    indice=list.index(lista,n)
    fatiado=lista[indice+1:]
    return fatiado