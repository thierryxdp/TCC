def acima_da_media(lista_numero):
    """Retorna, dados uma lista ordenada de numeros inteiros e um numero inteiro n, n na posição correta, deixando a lista ordenada
       Entrada: list, int;
       Saida: list;
    """
    n= sum(lista_numero)
    p= len(lista_numero)
    c= n/p
    if c in lista_numero:
        lista_numero.append(c)
        lista_numero.sort()
        y=list.index(lista_numero,c)
        b= lista_numero[y+2:]
        return b
    else:
        lista_numero.append(c)
        lista_numero.sort()
        y=list.index(lista_numero,c)
        b= lista_numero[y+1:]
        return b