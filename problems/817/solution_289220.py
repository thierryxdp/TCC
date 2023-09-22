def acima_da_media(lista):
    """Funcao que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordena com que as notas q ficaram acima da media, lista->list"""
    media=sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    posicao= list.index(lista,media)
    if media in lista:
        return lista[posicao+1:]
    else:
        return lista[posicao+2:]