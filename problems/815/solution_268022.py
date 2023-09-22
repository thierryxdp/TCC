def insere(lista_de_numeros,n):
    """Esta é a função que dado um número e uma lista ordenada de números inteiros ordena os números em ordem crescente e adiciona o número n na posição correta, list, int -> list"""
    lista = lista_de_numeros + [n]
    lista1 = sorted(lista)
    
    return lista1