def faltante(lista):
    """Retornar uma função que dada uma lista com n-1 inteiros numerados de 1 a N, descubra qual n° inteiro do intervalo está faltando; list=>list"""
	p = 0
    n = 0
    e = 0
    soma = (((1+(len(lista)+1))*(len(lista)+1))/2)
    list.sort(lista)
    while p<len(lista):
        if sum(lista) !som:
            n = (soma)-sum(lista)
            p += 1
            e += 1
    return n