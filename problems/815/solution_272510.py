def insere(lista,n):

    """
        Função que recebe uma lista e um número e coloca esse número na posição correta
        (1) A função vai ordenar a lista de entrar e vair retornar uma lista com o numero se entrda inserido na posição correta
        (2) Como o probelma pediu para retornar uma nova lista, foi criado a variável lista_final que, inicialmente, é uma copia da lista de entrada
        
        list, int or float --> list
        
    """
    lista_final = lista
    lista_final.append(n)
    lista_final.sort()
    return lista