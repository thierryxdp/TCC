def maiores(lista,numero):
    """Função copia a lista para uma nova, adiciona o numero recebido
    pela função a esta lista (caso este já não esteja na lista)
    e coloca os elementos em ordem crescente. Após isso,
    deleta da lista nova os elementos anteriores ao numero e ele mesmo
    Retorna a lista final.
    lista, int-> lista"""
    lista_maior=lista
    if numero not in lista:
    	lista_maior+=[numero]
    lista_maior.sort()
    posicao=lista_maior.index(numero)
    del lista_maior[:posicao+1]
    return lista_maior