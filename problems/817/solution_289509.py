def acima_da_media (lista):
    """Função que dada uma lista com notas dos alunos da turma, retorna uma lista ordenada com as notas que ficaram acima da média para aprovação que é igual a 5;
       list -> list."""
    list.sort (lista)
    import math
    lista_nova = sum (lista)/ len (lista)
    if lista_nova in lista == True:
        return lista [lista_nova:]
    else:
        a= math.ceil (lista_nova)
        b= list.index (lista, a)
        return lista [b:]