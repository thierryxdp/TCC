def maiores(lista_numero,n):
    """Funcao que, dados uma lista e um numero inteiro n, retorna uma nova lista
    com todos os numeros maiores que n;
    Entrada: list, int
    Saida: list"""
    
    lista = lista_numero + [n]
    list.sort(lista)
    posicao=list.index(lista)
    return lista[posicao:]