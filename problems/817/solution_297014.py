def acima_da_media(lista):
    """ Função que dada uma lista com notas de alunos retorna uma lista
    com as notas no sentido crescente
    list -> list"""
    lista1 = []
    contador = 0
    tamanho = len(lista)
    media = sum(lista) // tamanho

    while contador < tamanho:
        if lista[contador] > media:
            lista1 = lista1 + [lista[contador]]
        contador = contador + 1
	
   
    return  sorted(lista1)