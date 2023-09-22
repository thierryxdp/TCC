def acima_da_media(lista):
    '''dada uma lista com notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da media
    lista -> lista'''
    listaNova = list.sort(lista)
    med = sum(listaNova) / len(listaNova) 
    x = list.index(listaNova, med)
    return listaNova[x+1:]