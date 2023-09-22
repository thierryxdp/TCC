def acima_da_media(lista):
    """dada uma lista com notas de alunos, a função retorna uma nova lista
ordenada contendo as notas que ficaram acima da média.
list-->list

Parâmetros
lista: lista inicial com as notas dos alunos"""
    media=sum(lista)/len(lista)
    adiciona_media=list.append(lista,media)
    ordena_notas=list.sort(lista)
    if list.count(lista,media)==1:
        return lista[list.index(lista,media)+1:]
    else:
        return lista[list.index(lista,media)+2:]