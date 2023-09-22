def media (lista_notas):
    "Função que com a nota dos alunos da turma, retorne a media e uma lista com as notas acima da média; list->tuple"
    media = (sum(lista_notas))/len(lista_notas)
    if media not in lista_notas: 
        return (media, maiores(lista_notas,media))
    else:
        list.remove(lista_notas,media)
        return (media,maiores(lista_notas,media))