def acima_da_media (lista):
    """Função que dada uma lista com notas dos alunos da turma, retorna uma lista ordenada com as notas que ficaram acima da média para aprovação que é igual a 5;
       list -> list."""
    list.sort (lista)
    import math
    media = sum (lista)/ len (lista)
    if media in lista:
        lista_nova= list.index (lista, media)
        return lista [lista_nova+1:]
    else:
        list.append (lista, media)
        list.sort (lista)
        b= list.index (lista, media)
        return lista [b+1:]