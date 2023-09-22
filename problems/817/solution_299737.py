def acima_da_media(lista):
    """Função que, dada uma lista com as notas dos alunos
    de uma turma, retorne uma lista ordenada com as notas
    que ficaram acima da média.
    lista->lista."""
    lista2=[]
    for i in lista:
        if i > ((sum(lista))/len(lista)):
            lista2.append(i)
            list.sort(lista2)
    return lista2