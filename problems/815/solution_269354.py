def insere(lista_numero,n):
    """Retorna a lista ordenada(crescente) de numeros interiros com o 
    numero n na posicao correta dados: a lista de numeros(lista_numeros)
    e n"""
   
    lista_numero.append(n)
    lista=lista_numero.sort()
    return lista