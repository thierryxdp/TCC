def acima_da_media(lista_notas):
    '''A função recebe uma lista com as notas dos alunos de uma turma (valores
numéricos float) e retorna uma lista ordenada com as notas acima da média,
considerando a média igual a 7.0.
    Parâmetro de entrada: list
    Valor de retorno: list'''
    #Adicionado a nota média (7.0) à lista
    lista_notas=lista_notas+[7.0]
    #Ordenando a lista
    list.sort(lista_notas)
    #Indicando a posição de n na lista
    i=list.index(lista_notas,7.0)
    #Contando quantas vezes n aparece na lista
    vezes=list.count(lista_notas,7.0)
    #Formando a lista de números maiores que n
    lista_acima_da_media=lista[i+vezes::]
    return lista_acima_da_media