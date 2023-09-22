def acima_da_media(lista):
    """ Função que dada uma lista com notas de alunos retorna uma lista
    com as notas no sentido crescente
    list -> list"""    
    tamanho = len(lista)
    media = int(sum(lista)//tamanho)
    lista1 = maiores(lista,media+1)
    lista2 = sorted(lista1)
     
    
    return   lista2