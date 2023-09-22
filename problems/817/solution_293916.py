def acima_da_media(lista_numero):
    """Retorna, dados uma lista ordenada de numeros inteiros e um numero inteiro n, n na posição correta, deixando a lista ordenada
       Entrada: list, int;
       Saida: list;
    """
    n= sum(lista_numero)
    p= len(lista_numero) -1
    c= n/p
    lista_numero.append(p)
    lista_numero.sort()
	y=list.index(lista_numero,p)
    b= lista_numero[y+1:]
    return b