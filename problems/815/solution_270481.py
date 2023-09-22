def insere(lista_numero,n):
    """essa funcao calcula e retorna uma lista ordenada (crescente) de numero inteiros em um numero inteiro n, inclua n na posicao. de tal maneira que a lista continua ordenada; list, int -> list"""
    lista_numero.append(n)
    lista_numero.sort() 
    return lista_numero