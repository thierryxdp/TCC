def insere(lista_numero,n):
    """funcao que dada uma lista ordenada (crescente) de 
    numeros inteiros e um numero inteiro n de entrada,
    inclue n na posicao correta e retorna a nova lista;
    list, int -> list"""
    
    return list.sort(lista_numero + [n])