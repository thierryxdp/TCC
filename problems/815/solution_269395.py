def insere(lista_numero, n):
'''Funcao que dada uma lista ordenada crescente de numeros inteiros, 
recebeo numero inteiro (n) e retorna a lista ainda ordenada com (n) na 
posicao correta'''
    # Adiciona numero na lista na posicao final
    lista_numero.append(n)
    # Ordena a lista
    lista_numero.sort()
    
    # Retorna a lista ordenada
    return lista_numero