def acima_da_media(notas):
    alunos=len(notas)
    somaNotas=sum(notas)
    media=somaNotas/alunos
    list.append(notas,media)
    list.sort(notas)
    if alunos>1:
        excluir=list.index(notas,media)
        excluido=excluir+1
        maioresqmedia=notas[excluido:]
        return maioresqmedia
    else:
        excluir=list.index(notas,media)
        excluido=excluir+2
        maioresqmedia2=notas[excluido:]
        return maioresqmedia2