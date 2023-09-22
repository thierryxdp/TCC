def acima_da_media(lista_notas):
    '''dada uma lista com as notas dos alunos
de uma turma, retorna uma lista ordenada com as notas que ficaram acima da media.'''
    media = sum(lista_notas)/len(lista_notas)
    
    ssegunda_lista = []
    soma = 0

    for x in lista_notas:
        if x >= media:
            segunda_lista.append(x)

    for x in segunda_lista:
        soma += x
     
    ordenada = list.sort(segunda_lista)
    return segunda_lista