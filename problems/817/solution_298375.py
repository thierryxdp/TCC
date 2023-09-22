def acima_da_media (lista_notas):
    '''Dada uma lista com as notas dos alunos de uma
       turma, retorne uma nova lista em ordem com as que
       ficaram acima da média;
       list -> list'''
    l1 = sum(lista_notas)
    l2 = len(lista_notas)
    l3 = l1/l2
    return l3