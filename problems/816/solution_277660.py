def maiores(lista,n):
    """retorna uma lista que contem todos os 
    numeros da lista original maiores que um numero dado n"""
    lista_saida = []
    for i in lista:
        if n < i:
            lista_saida.append(i)
    lista_saida.sort()
    return lista_saida