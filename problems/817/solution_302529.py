def acima_da_media(lista_nota_turma):
    media_turma=sum(lista_nota_turma)//len(lista_nota_turma)
    lista_nota_turma1=lista_nota_turma+[media_turma]
    list.sort(lista_nota_turma1)
    x=lista_nota_turma1.index(media_turma)
    maiores_notas=lista_nota_turma1[x+1:]
    return maiores_notas