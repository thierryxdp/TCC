def acima_da_media(lista:list)->list:
    """ A funcao recebe uma lista de numeros inteiros, referente a nota dos alunos de uma turma. E retorna uma lista ordenada, com as notas que ficaram acima da media. A media é feita pela divisao da soma das notas, pela quantidade de notas """
    soma_das_notas = sum(lista)
    quantidade_numeros = len(lista)
    media = float(soma_das_notas / quantidade_numeros)
    list.append(lista,media)
    list.sort(lista)
    indice_media = list.index(lista,media)
    return indice_media+1