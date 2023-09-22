def acima_da_media(lista):
    media=sum(lista)/len(lista)
    if media not in lista:
        lista.append(media)
    lista.sort()
    x=lista.index(media)
    lista_2=lista[x+1:]
    y=lista_2.count(media)
    return lista_2[y:]
'''funcao que recebe a lista com a nota de alunos de uma turma e retorna uma lista ordenada com as notas que estao acima da media.
entrada:list
saida:list'''