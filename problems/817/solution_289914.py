def maiores(lista,n):
    list.sort(lista)
    posicao=list.index(lista,n)

    return lista[posicao+1:]

def acima_da_media(notas):
    """Calcula a media das notas e retorna uma lista ordenada com as notas
       acima da media;
       list->list
       Parametros:
       notas: notas dos alunos
    """
    media=(sum(notas))/len(notas)
    
    return maiores(notas,media)