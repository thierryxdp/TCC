def acima_da_media(lista):
    """Dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com
    as notas que ficaram acima da média,list->list"""
    contador=0
    acima=[]
    list.sort(lista)
    a=sum(lista)//len(lista)
    while contador<len(lista):
        if lista[contador]>a:
            list.append(acima,lista[contador])
        contador=contador+1
    return acima