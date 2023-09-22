def acima_da_media(notas):
    '''
    funcao que recebe uma lista com as notas
    dos alunos de uma turma e retorna uma
    lista ordenada com as notas que ficaram
    acima da media
    list->list
    '''
    calculo_media=sum(notas)//len(notas)
    notas.append(calculo_media)
    crescente=sorted(notas)
    posicao=crescente.index(calculo_media)
    lista=crescente[posicao+1:].copy()
    if calculo_media in lista:
    	del lista_nova[0]
    return lista