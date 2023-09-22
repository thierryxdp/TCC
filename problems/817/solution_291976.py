def acima_da_media(notas):
    '''recebe uma lista contendo notas de alunos e retorna uma lista com as notas acima da média.
    list -> list'''
    media = sum(notas)//len(notas)
    insere = list.append(notas,media)
    ordena_int = list.sort(notas)
    posicao = list.index(notas,media)
    lista = notas[posicao+1:]
    
    if media in lista:
        remove_elemento = list.remove(notas,media)
        return notas[posicao+1:]
    else:
        return notas[posicao+1:]