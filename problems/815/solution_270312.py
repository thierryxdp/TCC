def insere(lista_numero,n):
    """Funcao que dada uma lista ordenada (crescente)
    de numeros inteiros lista_numero e um numero inteiro n,
    inclui n na posicao correta, ou seja, retorna uma nova
    lista tambem ordenada;
    lista,int->lista"""
    
    list.append(lista_numero,n)
    list.sort(lista_numero)
    
    return lista_numero