def acima da media(lista):
    '''Retorna uma lista com as notas dos alunos que ficaram acima da média
    lista -> lista'''
    soma= sum(lista)
    quantidade_notas = len(lista)
    media = soma / quantidade_notas
    novo_elemento = list.append(media)
    lista_final = lista[novo_elemento+1:]
    return lista_final