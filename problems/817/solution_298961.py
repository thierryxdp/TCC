def acima_da_media(lista):
    """ Função que dada uma lista com notas de alunos retorna uma lista
    com as notas no sentido crescente
    list -> list"""
    tamanho = len(lista)
    media = sum(lista) // tamanho
    lista1 = sorted(lista) 
    list2 = lista1.index(media)
   
    return  lista1[media-1::]