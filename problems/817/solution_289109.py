def acima_da_media(lista):
    '''dada uma lista com notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da media
    lista -> lista'''
    listaNova = list.sort(lista)
    a = sum(listaNova)
    b = len(listaNova)
    media = a/b
    listaProblema = listaNova + [media]
    list.sort(listaProblema)
    x = list.index(listaProblema, med)
    return listaNova[x+1:]