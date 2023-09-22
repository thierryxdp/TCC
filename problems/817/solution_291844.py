def acima_da_media(lista_notas):
    '''A função recebe uma lista com as notas dos alunos de uma turma (valores
numéricos float) e retorna uma lista ordenada com as notas acima da média da
turma.
    Parâmetro de entrada: list
    Valor de retorno: list'''
    #Calculando a média
    media=sum(lista_notas)/len(lista_notas)
    #Adicionado a média à lista
    lista_notas=lista_notas+[media]
    #Ordenando a lista
    list.sort(lista_notas)
    #Indicando a posição de n na lista
    i=list.index(lista_notas,media)
    #Contando quantas vezes n aparece na lista
    vezes=list.count(lista_notas,media)
    #Formando a lista de números maiores que n
    lista_acima_da_media=lista_notas[i+vezes::]
    return lista_acima_da_media